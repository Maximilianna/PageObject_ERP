from Website.page_objects.MessagePage import MessagePage
from Website.page_elements.Manage import *


class ManagePage(MessagePage):

    def label_name(self):
        return "商品管理"

    # 点击商品管理按钮
    def click_Spgl(self):
        self.click_element(type_Manage)

    # 新增商品输入商品名字
    def input_add_name(self, name):
        self.input_element(type_name, name)

    # 新增商品选择商品分类
    def input_category(self, Class):
        self.select_element(type_category, Class)

    # 新增商品选择商品品牌
    def input_Brand(self, Brand):
        self.select_element(type_brand, Brand)

    # 新增商品选择商品单位
    def input_Unit(self, Unit):
        self.ul_input(Unit, type_unit, type_unit_ul)

    # 新增商品输入采购价格
    def input_add_Purchase(self, purchase):
        self.input_element(type_purchase, purchase)

    # 新增商品输入销售价格
    def input_add_Sale(self, sale):
        self.input_element(type_sale, sale)

    # 新增商品上传图片
    def input_file(self, fileAdd):
        self.input_element(type_file, fileAdd)

    # 新增商品点击保存按钮
    def click_Save_button(self):
        self.click_element(type_save)

    # 新增商品点击保存并新增按钮
    def click_SaveNew_button(self):
        self.click_element(type_saveNew)

    # 新增商品点击取消按钮
    def click_Cancel_button(self):
        self.click_element(type_cancel)

    # 查询商品输入商品编号或商品名
    def input_query_name(self, Name):
        self.input_element(type_query_Name, Name)

    # 查询商品选择商品分类
    def input_query_category(self, Price):
        self.select_element(type_query_category, Price)

    # 查询商品选择商品品牌
    def input_query_brand(self, Brand):
        self.select_element(type_query_brand, Brand)

    # 查询商品选择状态
    def input_query_status(self, Status):
        self.ul_input(Status, type_status, type_status_ul)

    # 时间格式：yyyy-MM-dd HH-mm-ss
    # 查询商品选择创建时间
    def input_create_date(self, startDate, endDate):
        self.input_element(type_create_start_date, startDate)
        self.input_element(type_create_end_date, endDate)

    # 查询商品选择修改时间
    def input_modify_date(self, startDate, endDate):
        self.input_element(type_modify_start_date, startDate)
        self.input_element(type_modify_end_date, endDate)

    # 修改商品，输入商品名字
    def click_modify_name(self, name):
        self.find_element(type_name).clear()
        self.input_add_name(name)

    # 修改商品，输入商品采购价格
    def click_modify_Purchase(self, purchase):
        self.find_element(type_purchase).clear()
        self.input_add_Purchase(purchase)

    # 修改商品，输入商品采购价格
    def click_modify_Sale(self, sale):
        self.find_element(type_sale).clear()
        self.input_add_Sale(sale)
