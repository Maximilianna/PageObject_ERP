from Website.page_objects.MessagePage import MessagePage
from Website.page_elements.Category import *


class CategoryPage(MessagePage):
    def click_Category(self):
        self.click_element(type_Category)
