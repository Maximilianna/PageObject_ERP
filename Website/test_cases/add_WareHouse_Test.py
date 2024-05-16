from Website.page_objects.LoginPage import Login
from Website.page_objects.WareHousePage import WareHousePage
from Website.model.myunit import TestMyUnit
from time import sleep

class add_WareHouse(TestMyUnit):
    def test(self):
        Login(self.driver, "XTGLY", "123456")
        warehouse_page = WareHousePage(self.driver)
        warehouse_page.into_page()
        sleep(2)
        warehouse_page.click_new()
        sleep(1)
        warehouse_page.input_add_name("仓库14")
        warehouse_page.input_Commissioner(14)
        warehouse_page.input_PhoneNumber("15142113182")
        warehouse_page.input_Address("辽宁省沈阳市沈北新区建设南一路")
        sleep(5)
