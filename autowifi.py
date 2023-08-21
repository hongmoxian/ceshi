import pywifi
from pywifi import const

def connect_to_wifi(ssid, password):
    wifi = pywifi.PyWiFi()
    iface = wifi.interfaces()[0]  # 获取第一个WiFi接口

    iface.scan()  # 扫描可用WiFi网络
    scan_results = iface.scan_results()

    # 在扫描结果中查找指定的WiFi网络
    target_network = None
    for result in scan_results:
        if result.ssid == ssid:
            target_network = result
            break

    if target_network:
        profile = pywifi.Profile()
        profile.ssid = ssid
        # profile.auth = const.AUTH_ALG_OPEN  # 开放认证方式
        # profile.akm.append(const.AKM_TYPE_WPA2PSK)  # WPA/WPA2 PSK加密
        # profile.cipher = const.CIPHER_TYPE_CCMP  # 加密算法

        profile.key = password  # WiFi密码

        iface.remove_all_network_profiles()  # 删除所有网络配置文件
        tmp_profile = iface.add_network_profile(profile)  # 添加新的网络配置文件

        iface.connect(tmp_profile)  # 连接WiFi
        # iface.disconnect()  # 断开连接，以便下次使用系统的网络管理连接

        return True
    else:
        return False

# 替换为您要连接的WiFi名称和密码
wifi_ssid = "henu"
wifi_password = ""

if connect_to_wifi(wifi_ssid, wifi_password):
    print("Connected to WiFi:", wifi_ssid)
else:
    print("Failed to connect to WiFi:", wifi_ssid)
import requests

# 替换为实际的登录页面URL、用户名和密码
login_url = "http://172.22.255.18/srun_portal_pc?ac_id=1&theme=pro"
username = "104753201286"
password = "9382275q."

# 创建会话
session = requests.Session()

# 访问登录页面，获取必要的信息（如CSRF令牌、Cookie等）
response = session.get(login_url)
csrf_token = response.cookies.get('csrftoken')

# 构建POST请求的数据
login_data = {
    'csrfmiddlewaretoken': csrf_token,
    'username': username,
    'password': password
}

# 发送登录请求
login_response = session.post(login_url, data=login_data)

# 检查是否登录成功（您可能需要根据实际情况进行判断）
if "欢迎登录" in login_response.text:
    print("登录成功")
else:
    print("登录失败")

from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://mail.163.com')
import requests

# 替换为实际的登录页面URL、用户名和密码
login_url = "http://172.22.255.18/srun_portal_pc?ac_id=1&theme=pro"
username = "104753201286"
password = "9382275q."
session = requests.Session()

# 访问登录页面，获取必要的信息（如CSRF令牌、Cookie等）
response = session.get(login_url)
login_data = {
    # 'csrfmiddlewaretoken': csrf_token,
    'username': username,
    'password': password
}

# 发送登录请求
login_response = session.post(login_url, data=login_data)

# 检查是否登录成功（您可能需要根据实际情况进行判断）
if "欢迎登录" in login_response.text:
    print("登录成功")
else:
    print("登录失败")
# csrf_token = response.cookies['csrftoken']
import selenium.webdriver as webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from time import sleep


# 替换为实际的登录页面URL、用户名和密码
login_url = "http://172.22.255.18/srun_portal_pc?ac_id=1&theme=pro"
username = "104753201286"
password = "9382275q."

# 使用指定的浏览器驱动，例如Chrome或Firefox
driver = webdriver.Chrome()

# 打开登录页面
driver.get(login_url)

# 找到用户名和密码输入框，并输入对应的信息
username_field = driver.find_element(By.ID,"username")
sleep(5)
password_field = driver.find_element(By.ID,"password")
sleep(5)
username_field.send_keys(username)
sleep(5)
password_field.send_keys(password)

sleep(5)
# 提交表单
login = driver.find_element(By.ID,"login-account")
login.send_keys(Keys.RETURN)

# 等待登录完成（可以根据实际情况调整等待时间或条件）
driver.implicitly_wait(10)

# 检查是否登录成功（您可能需要根据实际情况进行判断）
if "欢迎登录" in driver.page_source:
    print("登录成功")
else:
    print("登录失败")

# 关闭浏览器窗口
driver.quit()
driver = webdriver.Chrome()
driver.get(login_url)