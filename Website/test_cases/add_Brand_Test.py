from Website.page_objects.BrandPage import BrandPage
from Website.page_objects.LoginPage import Login
from Website.model.myunit import TestMyUnit
from Website.model.function import *
from ddt import ddt, data, unpack
from time import sleep


@ddt
class add_Brand(TestMyUnit):
    @data(*get_data_csv(f"..\\test_datas\\add_Brand_Test.csv"))
    @unpack
    def test_add_Brand(self, brandName):
        brand_page = BrandPage(self.driver)
        Login(self.driver, "XTGLY", "123456")
        sleep(3)
        brand_page.into_page()
        sleep(1)
        brand_page.click_new()
        sleep(1)
        brand_page.input_add_name(brandName)
        brand_page.click_save()
        sleep(2)
