from Website.page_objects.MessagePage import MessagePage
from Website.page_elements.Manage import *


class Manage(MessagePage):

    def label_name(self):
        return "商品管理"

    # 点击商品管理按钮
    def click_Spgl(self):
        self.click_element(type_Manage)

    # 点击新增按钮
    def click_new(self):
        self.click_element(type_new)

    # 新增商品输入商品名 可变参数key：1：清空原本内容
    def input_Name(self, name, *key):
        e = self.find_element(type_add_name)
        if len(key) != 0 and key[0] != 0:
            e.clear()
        e.send_keys(name)

    # 新增商品选择商品分类
    def input_category(self, Class):
        self.select_element(type_add_category, Class)

    # 新增商品选择商品品牌
    def input_Brand(self, Brand):
        self.select_element(type_add_brand, Brand)

    # 新增商品选择商品单位
    def input_Unit(self, Unit):
        self.ul_input(Unit, type_unit, type_unit_ul)

    # 新增商品输入采购价格 可变参数key：1：清空原本内容
    def input_Purchase(self, purchase, *key):
        e = self.find_element(type_purchase)
        if len(key) != 0 and key[0] != 0:
            e.clear()
        e.send_keys(purchase)

    # 新增商品输入销售价格 可变参数key：1：清空原本内容
    def input_Sale(self, sale, *key):
        e = self.find_element(type_sale)
        if len(key) != 0 and key[0] != 0:
            e.clear()
        e.send_keys(sale)

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

    # 查询商品点击查询按钮
    def click_query_button(self):
        self.click_element(type_query_button)

    # 查询商品点击重置按钮
    def click_reset_button(self):
        self.click_element(type_reset_button)

    # 点击修改按钮
    def click_data_modify(self, index):
        type_data_modify_start[1] = (type_data_modify_start[1]
                                     + str(index)
                                     + type_data_modify_end[1])
        self.click_element(type_data_modify_start)

    # 点击禁用或启用按钮
    def click_disable_open(self, index):
        type_date_disable_open_start[1] = (type_date_disable_open_start[1]
                                           + str(index)
                                           + type_date_disable_open_end[1])
        self.click_element(type_date_disable_open_start)

    # 确定禁用或启用
    def click_disable_open_accept(self):
        self.alert_accept()

    # 取消禁用或启用
    def click_disable_open_dismiss(self):
        self.alert_dismiss()
