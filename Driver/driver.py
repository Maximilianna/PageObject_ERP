from selenium import webdriver
from selenium.webdriver.chrome.service import Service


def get_driver():
    # 需要将chromedriver.exe文件放在指定的路径
    service = Service(r"D:\chromedriver.exe")
    driver = webdriver.Chrome(service=service)
    return driver
