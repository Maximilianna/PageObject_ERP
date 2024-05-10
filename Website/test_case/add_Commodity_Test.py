from Website.model.myunit import TestMyUnit
from Website.model.function import get_data_csv
from Website.page_object.LoginPage import LoginPage
from Website.page_object.SpglPage import SpglPage
from time import sleep
from ddt import ddt, data, unpack

@ddt
class add_Test(TestMyUnit):
    @data(*get_data_csv())
    @unpack
    def test_add_Test(self, Name, Class, Brand, Unit, Purchase, Sale):
        loginpage = LoginPage(self.driver)
        spglpage = SpglPage(self.driver)
        loginpage.open("http://10.255.4.105:14753/login")
        loginpage.input_username("XTGLY")
        loginpage.input_password("123456")
        loginpage.click_login()
        spglpage.click_new()
        spglpage.input_Name(Name)
        spglpage.input_Class(Class)
        spglpage.input_Brand(Brand)
        spglpage.input_Unit(Unit)
        spglpage.input_Purchase(Purchase)
        spglpage.input_Sale(Sale)
        spglpage.click_SaveNew_button()
        sleep(3)
