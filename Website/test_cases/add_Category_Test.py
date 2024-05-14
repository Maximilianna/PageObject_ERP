from Website.page_objects.LoginPage import Login
from Website.page_objects.CategoryPage import CategoryPage
from Website.model.myunit import TestMyUnit
from time import sleep

class add_Category(TestMyUnit):
    def test(self):
        Login(self.driver, "XTGLY", "123456")
        category_page = CategoryPage(self.driver)
        sleep(5)
        category_page.into_page()
        sleep(1)
        category_page.click_new()
        sleep(1)
        category_page.input_add_name("bbbbb")
        category_page.click_save()
        sleep(5)
