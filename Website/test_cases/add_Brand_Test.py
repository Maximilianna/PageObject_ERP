from Website.page_objects.BrandPage import BrandPage
from Website.page_objects.LoginPage import Login
from Website.model.myunit import TestMyUnit
from time import sleep


class add_Brand(TestMyUnit):
    def test_add_Brand(self):
        brand_page = BrandPage(self.driver)
        Login(self.driver, "XTGLY", "123456")
        sleep(3)
        brand_page.click_Brand()
        sleep(1)
        brand_page.click_new()
        brand_page.input_add_brand_name("华为")
        brand_page.click_cancel_brand()
        sleep(1)
        brand_page.close_labels("商品管理")
        brand_page.input_query_brand_name("华为")
        brand_page.input_query_brand_status("启用")
        brand_page.click_query()
        sleep(1)
        brand_page.click_reset()
        brand_page.click_query()
        #brand_page.click_query_brand()
        #brand_page.input_records(20)
        brand_page.click_quick("next")
        sleep(1)
        brand_page.click_quick("prev")
        sleep(1)
        brand_page.click_number(5)
        sleep(3)
        brand_page.click_number(1)
        sleep(1)
        brand_page.click_data_modify(1)
        sleep(1)
        brand_page.input_modify_brand_name("华为")
        brand_page.click_save_brand()
        sleep(1)
        brand_page.click_data_switch(1)
        sleep(2)
        brand_page.data_switch_dismiss()
        sleep(2)
