from Website.page_objects.BasePage import BasePage
from Website.page_elements.Brand import *


class BrandPage(BasePage):

    # 点击商品品牌按钮
    def click_Brand(self):
        self.click_element(type_brand[0], type_brand[1])

    # 点击新增按钮
    def click_new_brand(self):
        self.click_element(type_new_brand[0],
                           type_new_brand[1])

    # 新增商品品牌，输入品牌名
    def input_brand_name(self, brand_name):
        self.input_element(type_brand_name[0],
                           type_brand_name[1], brand_name)

    # 新增商品品牌，点击保存按钮
    def click_save_brand(self):
        self.click_element(type_save_button[0], type_save_button[1])

    # 新增商品品牌，点击取消按钮
    def click_cancel_brand(self):
        self.click_element(type_cancel_button[0], type_cancel_button[1])
