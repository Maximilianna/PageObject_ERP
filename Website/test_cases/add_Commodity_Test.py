from Website.model.myunit import TestMyUnit
from Website.model.function import get_data_csv
from Website.page_objects.LoginPage import Login
from Website.page_objects.ManagePage import Manage
from time import sleep
from ddt import ddt, data, unpack

@ddt
class add_Test(TestMyUnit):
    @data(*get_data_csv(f"..\\test_datas\\add_Commodity_Test.csv"))
    @unpack
    def test_add_Test(self, Name, Class, Brand, Unit, Purchase, Sale):
        Login(self.driver, "XTGLY", "123456")
        manage_page = Manage(self.driver)
        manage_page.click_new()
        manage_page.input_Name(Name)
        manage_page.input_Class(Class)
        manage_page.input_Brand(Brand)
        manage_page.input_Unit(Unit)
        manage_page.input_Purchase(Purchase)
        manage_page.input_Sale(Sale)
        manage_page.click_SaveNew_button()
        sleep(3)
