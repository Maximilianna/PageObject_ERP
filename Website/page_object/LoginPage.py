from Website.page_object.BasePage import BasePage
from Website.page_element.Login import *


class LoginPage(BasePage):
    # 输入用户名
    def input_username(self, username):
        self.input_element(type_username[0],
                           type_username[1], username)

    # 输入密码
    def input_password(self, password):
        self.input_element(type_password[0],
                           type_password[1], password)

    # 点击登录按钮
    def click_login(self):
        self.click_element(type_button[0],
                           type_button[1])


def Login(driver, username, password):
    login_page = LoginPage(driver)
    login_page.open("http://10.255.4.105:14753/login")
    login_page.input_username(username)
    login_page.input_password(password)
    login_page.click_login()
