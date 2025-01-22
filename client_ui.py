import requests
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
    except Exception as e:
        print(f"无法获取系统代理设置: {e}")
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
    update_log = Signal(str)

    def __init__(self, urls, proxy_settings, headers):
        super().__init__()
        self.urls = urls
        self.proxy_settings = proxy_settings
        self.headers = headers

    def run(self):
        error_count = 0
        for url in self.urls:
            self.update_log.emit(f"测试：{url}")
            try:
                # 允许自动处理重定向
                response = requests.get(url, proxies=self.proxy_settings, headers=self.headers, timeout=4, allow_redirects=True)

                # 检查是否发生重定向
                if response.history:
                    self.update_log.emit(f"\n-> 重定向至：{response.url}")

                # 检查最终状态码
                if response.status_code == 200:
                    self.update_log.emit(f"  正常 (200)\n")
                else:
                    self.update_log.emit(f"  异常 ({response.status_code})\n")
                    error_count += 1
            except requests.exceptions.RequestException as e:
                self.update_log.emit(f"  失败 ({e})\n")
                error_count += 1

        self.update_log.emit(f"测试任务完成！成功个数：{len(self.urls) - error_count}/{len(self.urls)}\n")


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
        self.textEdit.clear()
        for url in urls:
            self.textEdit.append(url)
        self.textEdit.append("")
        if manual:
            QMessageBox.information(self, "提示", "配置文件已重新加载！")

    def save_config_to_file(self):
        text = self.textEdit.toPlainText()
        urls = [line.strip() for line in text.split('\n') if is_valid_url(line.strip())]
        with open("./config.txt", 'w') as file:
            for url in urls:
                file.write(url + '\n')
        QMessageBox.information(self, "提示", "配置文件已保存！")

    def start_test(self):
        # 清理日志
        self.textBrowser_log.clear()
        # 获取网址
        text = self.textEdit.toPlainText()
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
        self.thread.update_log.connect(self.update_log)
        self.thread.start()

    def update_log(self, message):
        self.textBrowser_log.insertPlainText(message)

if __name__ == "__main__":
    app = QApplication([])
    window = MainWindow()
    window.show()
    app.exec()

# 使用以下命令打包exe文件
# pyinstaller --onefile --noconsole --version-file=version.txt --icon=./icon.ico --add-data "icon.png;." client_ui.py
