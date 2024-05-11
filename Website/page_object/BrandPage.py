from Website.page_object.BasePage import BasePage
from Website.page_element.Brand import *


class BrandPage(BasePage):
    def click_Brand(self):
        self.click_element(type_brand[0], type_brand[1])