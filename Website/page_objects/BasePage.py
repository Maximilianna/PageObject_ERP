from selenium.webdriver.support.select import Select
from Website.page_elements.Base import *


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, My_type, name):
        return self.driver.find_element(My_type, name)

    def find_elements(self, My_type, name):
        return self.driver.find_elements(My_type, name)

    def click_element(self, My_type, name):
        self.find_element(My_type, name).click()

    def click_elements(self, My_type, name, index):
        self.find_elements(My_type, name)[index].click()

    def input_element(self, My_type, name, value):
        self.find_element(My_type, name).send_keys(value)

    def input_elements(self, My_type, name, value, index):
        self.find_elements(My_type, name)[index].send_keys(value)

    def select_element(self, My_type, name, My_str):
        Select(self.find_element(My_type, name)).select_by_visible_text(My_str)

    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()

    def close_labels(self, *labelName):
        labels = self.find_elements(type_labels[0], type_labels[1])
        for label in labels:
            if len(labels) < 2:
                print("标签页小于2页，无法关闭！")
                break
            if type(labelName[0]) == str and label.text == labelName[0]:
                label.find_element(type_label[0], type_label[1]).click()
                break
            elif label.text == self.label_name():
                label.find_element(type_label[0], type_label[1]).click()
                break

    # 需要继承类重写
    def label_name(self):
        return ""
