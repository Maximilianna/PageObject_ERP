from selenium import webdriver


def get_driver():
    driver = webdriver.Chrome()
    return driver
