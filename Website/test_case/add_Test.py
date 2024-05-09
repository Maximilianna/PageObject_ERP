from Website.test_case.model.myunit import TestMyUnit
from Website.test_case.page_object.LoginPage import LoginPage
from Website.test_case.page_object.SpglPage import SpglPage
from time import sleep

class add_Test(TestMyUnit):
    def test_add_Test(self):
        loginpage = LoginPage(self.driver)
        loginpage.open("http://10.255.4.105:14753/login")
        loginpage.input_username("XTGLY")
        loginpage.input_password("123456")
        loginpage.click_login()
        sleep(5)
        spglpage = SpglPage(self.driver)
        # spglpage.input_query_name("123")
        # spglpage.input_query_class("测试数据ee")
        # spglpage.input_query_brand("测试数据")
        # spglpage.click_new()
        # sleep(0.5)
        # spglpage.click_Cancel_button()
        # sleep(0.5)
        # spglpage.input_query_status("禁用")
        # spglpage.input_create_date("2022-01-01 12:00:00", "2023-01-01 12:00:00")
        # spglpage.input_modify_date("2023-01-01 12:00:00", "2023-01-01 12:00:00")
        # spglpage.click_query_button()
        # spglpage.input_records(20)
        # spglpage.click_pagination(393)
        # sleep(2)
        # spglpage.click_prev()
        # sleep(2)
        # spglpage.click_next()
        # sleep(2)
        spglpage.click_pagination(393)
        sleep(3)
        spglpage.click_pagination(389)
        sleep(3)
        spglpage.click_pagination_next()
        sleep(2)
