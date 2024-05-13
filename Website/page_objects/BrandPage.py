from Website.page_objects.MessagePage import MessagePage
from Website.page_elements.Brand import *


class BrandPage(MessagePage):

    def label_name(self):
        return "商品品牌"

    # 点击商品品牌按钮
    def click_Brand(self):
        self.click_element(type_brand)

    # 新增商品品牌，输入品牌名
    def input_add_brand_name(self, brandName):
        self.input_element(type_add_brand_name, brandName)

    # 新增商品品牌，点击保存按钮
    def click_save_brand(self):
        self.click_element(type_save_button)

    # 新增商品品牌，点击取消按钮
    def click_cancel_brand(self):
        self.click_element(type_cancel_button)

    # 查询商品品牌，输入品牌名
    def input_query_brand_name(self, brandName):
        self.input_element(type_query_brand_name, brandName)

    # 查询商品品牌，输入商品状态
    def input_query_brand_status(self, brandStatus):
        self.ul_input(brandStatus,
                      type_query_brand_status,
                      type_query_brand_ul)

    # 修改商品品牌，输入品牌名字
    def input_modify_brand_name(self, brandName):
        self.find_element(type_modify_brand_name).clear()
        self.input_add_brand_name(brandName)
