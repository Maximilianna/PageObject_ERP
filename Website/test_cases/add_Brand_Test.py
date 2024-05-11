from Website.page_objects.BrandPage import BrandPage
from Website.page_objects.LoginPage import Login
from Website.model.myunit import TestMyUnit
from time import sleep


class add_Brand(TestMyUnit):
    def test_add_Brand(self):
        brand_page = BrandPage(self.driver)
        Login(self.driver, "XTGLY", "123456")
        sleep(5)
        brand_page.click_Brand()
        sleep(3)
        brand_page.click_new_brand()
        brand_page.input_brand_name("华为")
        brand_page.click_cancel_brand()
        sleep(3)
