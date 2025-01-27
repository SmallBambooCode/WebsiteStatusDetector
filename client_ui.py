import requests
from requests.exceptions import RequestException, Timeout, ConnectionError, HTTPError, SSLError
from PySide6.QtCore import QThread, Signal
from PySide6.QtWidgets import QApplication, QMainWindow, QMessageBox
from PySide6.QtGui import QIcon
from MainWindow import Ui_MainWindow
import winreg
import sys
import os
import re


# 判断是否为打包后的环境
if getattr(sys, 'frozen', False):
    # 运行在打包后的环境中
    base_path = sys._MEIPASS  # 获取打包后的临时目录
else:
    # 运行在开发环境中
    base_path = os.path.abspath(".")  # 获取当前工作目录


def get_windows_proxy():
    """从Windows注册表中获取系统代理设置"""
    try:
        registry_key = winreg.OpenKey(winreg.HKEY_CURRENT_USER, r"Software\\Microsoft\\Windows\\CurrentVersion\\Internet Settings")
        proxy_enabled, _ = winreg.QueryValueEx(registry_key, "ProxyEnable")
        proxy_server, _ = winreg.QueryValueEx(registry_key, "ProxyServer")
        winreg.CloseKey(registry_key)

        if proxy_enabled:
            return {
                "http": f"http://{proxy_server}",
                "https": f"http://{proxy_server}",
            }
        else:
            return None
    except Exception:
        return None

# 验证网址是否为合法URL
def is_valid_url(url):
    # 改进后的正则表达式
    pattern = re.compile(
        r'^(https?|ftp):\/\/'  # 支持http、https、ftp协议
        r'(([a-zA-Z0-9-]+\.)+[a-zA-Z]{2,})'  # 域名部分（支持二级、三级及以上域名）
        r'(:\d+)?'  # 端口号（可选）
        r'(\/[^\s]*)?$',  # 路径部分（可选）
        re.IGNORECASE)
    return re.match(pattern, url) is not None

class TestUrlsThread(QThread):
    # 定义信号，用来更新UI
    test_started = Signal()
    update_log = Signal(str)
    update_progress_bar = Signal(int)
    roll_log = Signal()
    test_finished = Signal()

    def __init__(self, urls, proxy_settings, headers):
        super().__init__()
        self.urls = urls
        self.proxy_settings = proxy_settings
        self.headers = headers

    def run(self):
        # 开始测试前发出信号，锁定按钮
        self.test_started.emit()
        urls_num = len(self.urls)
        current_curls_num = 0
        error_count = 0
        for url in self.urls:
            self.update_log.emit(f"测试：{url}")
            try:
                # 允许自动处理重定向
                response = requests.get(url, proxies=self.proxy_settings, headers=self.headers, timeout=10, allow_redirects=True)

                # 检查是否发生重定向
                if response.history:
                    self.update_log.emit(f"\n-> 重定向至：{response.url}")

                # 检查最终状态码
                if response.status_code == 200:
                    self.update_log.emit(f"  正常 (200)\n")
                else:
                    self.update_log.emit(f"  异常 ({response.status_code})\n")
                    error_count += 1
            except Timeout:
                self.update_log.emit("  失败 (请求超时)\n")
                error_count += 1
            except SSLError:
                self.update_log.emit("  失败 (SSL证书过期或无效)\n")
                error_count += 1
            except ConnectionError as e:
                self.update_log.emit("  失败 (网络连接失败)\n")
                print(e)
                error_count += 1
            except HTTPError as e:
                self.update_log.emit(f"  失败 (HTTP 错误 {e.response.status_code})\n")
                error_count += 1
            except RequestException:
                self.update_log.emit("  失败 (请求失败)\n")
                error_count += 1

            current_curls_num += 1
            self.update_progress_bar.emit(int(current_curls_num/urls_num*100))
            # 完成一个网址的检测后就滚动到最下方
            self.roll_log.emit()

        self.update_log.emit(f"测试任务完成！成功个数：{len(self.urls) - error_count}/{len(self.urls)}")
        self.roll_log.emit()
        # 结束测试前发出信号，解锁按钮
        self.test_finished.emit()


class MainWindow(QMainWindow, Ui_MainWindow):
    def __init__(self):
        super().__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon(os.path.join(base_path, "icon.png")))
        self.put_normal_urls_on_textedit()

        # 绑定按钮
        self.pushButton_exit.clicked.connect(self.close)
        self.pushButton_read_config.clicked.connect(lambda: self.put_normal_urls_on_textedit(manual=True))
        self.pushButton_save_config.clicked.connect(self.save_config_to_file)
        self.pushButton_start.clicked.connect(self.start_test)


    def put_normal_urls_on_textedit(self, manual=False):
        # 确保文件存在
        if not os.path.exists("./config.txt"):
            with open("./config.txt", 'w') as file:
                pass  # 创建一个空文件
        with open("./config.txt", 'r') as file:
            urls = [line.strip() for line in file.readlines() if is_valid_url(line.strip())]
        self.textEdit_urls.clear()
        for url in urls:
            self.textEdit_urls.append(url)
        self.textEdit_urls.append("")
        if manual:
            QMessageBox.information(self, "提示", "配置文件已重新加载！")

    def save_config_to_file(self):
        text = self.textEdit_urls.toPlainText()
        urls = [line.strip() for line in text.split('\n') if is_valid_url(line.strip())]
        with open("./config.txt", 'w') as file:
            for url in urls:
                file.write(url + '\n')
        QMessageBox.information(self, "提示", "配置文件已保存！")

    def start_test(self):
        # 清理日志
        self.textBrowser_log.clear()
        self.progressBar_test.setValue(0)
        # 获取网址
        text = self.textEdit_urls.toPlainText()
        urls = [line.strip() for line in text.split('\n') if is_valid_url(line.strip())]
        if not urls:
            QMessageBox.warning(self, "警告", "请输入至少一个合法的网址！")
            return
        # 获取代理设置
        proxy_settings = get_windows_proxy()
        if proxy_settings:
            QMessageBox.information(self, "提示", "检测到系统代理，程序将自动启用代理检测网站！")
        # 设置User-Agent为正常的Chrome浏览器
        headers = {
            "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
        }
        # 创建并启动子线程
        self.thread = TestUrlsThread(urls, proxy_settings, headers)
        self.thread.test_started.connect(self.lock_start_button)
        self.thread.update_log.connect(self.update_log)
        self.thread.update_progress_bar.connect(self.update_progress_bar)
        self.thread.roll_log.connect(self.roll_log)
        self.thread.test_finished.connect(self.unlock_start_button)
        self.thread.start()


    def update_log(self, message):
        self.textBrowser_log.insertPlainText(message)

    def update_progress_bar(self, percentage):
        if 0 <= percentage <= 100:
            self.progressBar_test.setValue(percentage)

    def roll_log(self):
        self.textBrowser_log.verticalScrollBar().setValue(self.textBrowser_log.verticalScrollBar().maximum())

    def lock_start_button(self):
        self.pushButton_start.setEnabled(False)

    def unlock_start_button(self):
        self.pushButton_start.setEnabled(True)


if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

# 使用以下命令打包exe文件
# pyinstaller --onefile --noconsole --version-file=version.txt --icon=./icon.ico --add-data "icon.png;." client_ui.py
