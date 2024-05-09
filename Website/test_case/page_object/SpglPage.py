from Website.test_case.page_object.BasePage import BasePage
from Website.test_case.page_element.Spgl import *
from time import sleep


class SpglPage(BasePage):
    # 点击商品管理按钮
    def click_Spgl(self):
        self.click_element(type_Spgl[0],
                           type_Spgl[1])

    # 点击新增按钮
    def click_new(self):
        self.click_element(type_new[0],
                           type_new[1])

    # 新增商品输入商品名
    def input_Name(self, name):
        self.input_element(type_add_name[0],
                           type_add_name[1], name)

    # 新增商品选择商品分类
    def input_Class(self, Class):
        self.select_element(type_add_class[0],
                            type_add_class[1], Class)

    # 新增商品选择商品品牌
    def input_Brand(self, Brand):
        self.select_element(type_add_brand[0],
                            type_add_brand[1], Brand)

    # 新增商品选择商品单位
    def input_Unit(self, Unit):
        self.click_element(type_unit[0], type_unit[1])
        sleep(0.5)
        ul = self.find_element(type_unit_ul[0], type_unit_ul[1])
        li = ul.find_elements(type_unit_li[0], type_unit_li[1])
        for now in li:
            if now.text == Unit:
                now.click()
                break

    # 新增商品输入采购价格
    def input_Purchase(self, purchase):
        self.input_element(type_purchase[0],
                           type_purchase[1],
                           purchase)

    # 新增商品输入销售价格
    def input_Sale(self, sale):
        self.input_element(type_sale[0],
                           type_sale[1], sale)

    # 新增商品上传图片
    def input_file(self, fileAdd):
        self.input_element(type_file[0],
                           type_file[1], fileAdd)

    # 新增商品点击保存按钮
    def click_Save_button(self):
        self.click_element(type_save[0], type_save[1])

    # 新增商品点击保存并新增按钮
    def click_SaveNew_button(self):
        self.click_element(type_saveNew[0], type_saveNew[1])

    # 新增商品点击取消按钮
    def click_Cancel_button(self):
        self.click_element(type_cancel[0], type_cancel[1])

    # 查询商品输入商品编号或商品名
    def input_query_name(self, Name):
        self.input_element(type_query_Name[0],
                           type_query_Name[1], Name)

    # 查询商品选择商品分类
    def input_query_class(self, Price):
        self.select_element(type_query_class[0],
                            type_query_class[1], Price)

    # 查询商品选择商品品牌
    def input_query_brand(self, Brand):
        self.select_element(type_query_brand[0],
                            type_query_brand[1], Brand)

    # 查询商品选择状态
    def input_query_status(self, Status):
        self.click_element(type_status[0], type_status[1])
        sleep(0.5)
        ul = self.find_element(type_status_ul[0], type_status_ul[1])
        li = ul.find_elements(type_status_li[0], type_status_li[1])
        for now in li:
            if now.text == Status:
                now.click()
                break

    # 时间格式：yyyy-MM-dd HH-mm-ss
    # 查询商品选择创建时间
    def input_create_date(self, startDate, endDate):
        self.input_element(type_create_start_date[0],
                           type_create_start_date[1], startDate)
        self.input_element(type_create_end_date[0],
                           type_create_end_date[1], endDate)

    # 查询商品选择修改时间
    def input_modify_date(self, startDate, endDate):
        self.input_element(type_modify_start_date[0],
                           type_modify_start_date[1], startDate)
        self.input_element(type_modify_end_date[0],
                           type_modify_end_date[1], endDate)

    # 查询商品点击查询按钮
    def click_query_button(self):
        self.click_element(type_query_button[0],
                           type_query_button[1])

    # 查询商品点击重置按钮
    def click_reset_button(self):
        self.click_element(type_reset_button[0],
                           type_reset_button[1])

    # 设置每页显示多少条记录
    def input_records(self, value):
        self.click_element(type_records[0],
                           type_records[1])
        sleep(0.5)
        ul = self.find_elements(type_records_child[0],
                                type_records_child[1])[-1].find_element(By.XPATH, "..")
        li = ul.find_elements(type_records_li[0],
                              type_records_li[1])
        for now in li:
            if now.text == str(value) + "条/页":
                now.click()
                break

    # 点击指定页数按钮
    def click_pagination(self, value):
        ul = self.find_element(type_pagination[0],
                                type_pagination[1]).find_element(By.XPATH, "ul")
        li = ul.find_elements(type_pagination_li[0],
                              type_pagination_li[1])
        for now in li:
            if now.text == str(value):
                now.click()
                break

    # 点击上一页按钮
    def click_prev(self):
        self.click_element(type_prev[0], type_prev[1])

    # 点击下一页按钮
    def click_next(self):
        self.click_element(type_next[0], type_next[1])

    # 在分页栏点击快速向前
    def click_pagination_prev(self):
        current = self.find_element(type_pagination_current[0],
                                    type_pagination_current[1])
        ul = self.find_element(type_pagination[0],
                               type_pagination[1]).find_element(By.XPATH, "ul")
        li = ul.find_elements(type_pagination_li[0],
                              type_pagination_li[1])
        if int(current.text) > int(li[0].text) + 3:
            li[1].click()

    # 在分页栏点击快速向后
    def click_pagination_next(self):
        current = self.find_element(type_pagination_current[0],
                                    type_pagination_current[1])
        ul = self.find_element(type_pagination[0],
                               type_pagination[1]).find_element(By.XPATH, "ul")
        li = ul.find_elements(type_pagination_li[0],
                              type_pagination_li[1])
        if int(current.text) < int(li[-1].text) - 3:
            li[7].click()
