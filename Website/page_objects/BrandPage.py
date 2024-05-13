from Website.page_objects.BasePage import BasePage
from Website.page_elements.Brand import *
from time import sleep


class BrandPage(BasePage):

    def label_name(self):
        return "商品品牌"

    # 点击商品品牌按钮
    def click_Brand(self):
        self.click_element(type_brand)

    # 点击新增按钮
    def click_new_brand(self):
        self.click_element(type_new_brand)

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

    # 查询商品品牌，点击查询按钮
    def click_query_brand(self):
        self.click_element(type_query_brand)

    # 页面跳转器
    def input_records(self, value):
        Str = str(value) + "条/页"
        self.ul_input(Str, type_records, type_records_ul)

    # 在分页栏点击快速向后
    def click_quick_next(self):
        self.click_quick(type_pagination_current,
                         type_pagination_entirety,
                         type_quick_next, 1)

    # 在分页栏点击快速向前
    def click_quick_prev(self):
        self.click_quick(type_pagination_current,
                         type_pagination_entirety,
                         type_quick_prev, -1)
