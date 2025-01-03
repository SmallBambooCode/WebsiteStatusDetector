import requests
import os
import sys
import winreg
import json

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

def test_websites(urls):
    """批量测试多个网站是否能通过系统代理或直接访问正常打开"""
    # 检查系统代理状态
    proxies = get_windows_proxy()
    if proxies:
        print("检测到系统代理已开启，使用以下代理:", proxies)
    else:
        print("未检测到系统代理，直接访问。")

    # 设置User-Agent为正常的Chrome浏览器
    headers = {
        "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/114.0.0.0 Safari/537.36"
    }

    for url in urls:
        print(f"测试网站: {url}")
        try:
            response = requests.get(url, proxies=proxies, headers=headers, timeout=10)
            if response.status_code == 200:
                print(f"网站 {url} 正常打开，状态码: {response.status_code}")
            else:
                print(f"网站 {url} 无法正常打开，状态码: {response.status_code}")
        except requests.exceptions.RequestException as e:
            print(f"无法访问网站 {url}，错误: {e}")

if __name__ == "__main__":
    if len(sys.argv) != 2:
        print("用法: python test_website_proxy.py <网站列表文件.json>")
        sys.exit(1)

    json_file = sys.argv[1]
    try:
        with open(json_file, "r", encoding="utf-8") as file:
            website_urls = json.load(file)
        if not isinstance(website_urls, list):
            print("JSON 文件格式错误，应为网址列表")
            sys.exit(1)
    except Exception as e:
        print(f"无法读取JSON文件: {e}")
        sys.exit(1)

    test_websites(website_urls)
