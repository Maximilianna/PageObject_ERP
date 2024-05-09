from Website.model.myunit import TestMyUnit
from Website.page_object.LoginPage import LoginPage
from Website.page_object.SpglPage import SpglPage
from time import sleep

from Website.page_object.SpppPage import SpppPage


class add_Test(TestMyUnit):
    def test_add_Test(self):
        loginpage = LoginPage(self.driver)
        loginpage.open("http://10.255.4.105:14753/login")
        loginpage.input_username("XTGLY")
        loginpage.input_password("123456")
        loginpage.click_login()
        
        sleep(3)
