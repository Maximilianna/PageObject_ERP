from Website.page_objects.BasePage import BasePage
from Website.page_elements.Brand import *


class BrandPage(BasePage):
    def click_Brand(self):
        self.click_element(type_brand[0], type_brand[1])