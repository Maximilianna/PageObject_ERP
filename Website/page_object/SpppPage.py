from Website.page_object.BasePage import BasePage
from Website.page_element.Sppp import *


class SpppPage(BasePage):
    def click_Sppp(self):
        self.click_element(type_sppp[0], type_sppp[1])