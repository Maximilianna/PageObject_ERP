from Website.page_objects.BasePage import BasePage
from Website.page_elements.Login import *


class LoginPage(BasePage):
    # 输入用户名
    def input_username(self, username):
        self.input_element(type_username, username)

    # 输入密码
    def input_password(self, password):
        self.input_element(type_password, password)

    # 点击登录按钮
    def click_login(self):
        self.click_element(type_button)


def Login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open("http://10.255.4.105:14753/login")
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login()
