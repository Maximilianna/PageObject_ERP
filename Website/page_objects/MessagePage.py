from Website.page_objects.LabelsPage import LabelsPage
from selenium.webdriver.common.keys import Keys
from time import sleep
from Website.page_elements.Base import *
import traceback


class MessagePage(LabelsPage):
    def ul_input(self, Options, Input_Location, li_Location):
        self.click_element(Input_Location)
        sleep(0.5)
        li = self.find_elements(li_Location)
        try:
            for now in li:
                if now.get_attribute("textContent") == Options:
                    now.click()
                    break
        except:
            traceback.print_exc()

    def click_quick(self, Str):
        current = self.find_element(type_pagination_current)
        if Str == "next":
            next = self.find_elements(type_pagination_entirety)[-1]
            if int(current.text) <= int(next.text) - 4:
                self.click_element(type_quick_next)
        elif Str == "prev":
            prev = self.find_elements(type_pagination_entirety)[0]
            if int(current.text) >= int(prev.text) + 4:
                self.click_element(type_quick_prev)

    def click_quick_next(self):
        self.click_quick("next")

    def click_quick_prev(self):
        self.click_quick("prev")

    # 点击上一页按钮
    def click_prev(self):
        self.click_element(type_prev)

    # 点击下一页按钮
    def click_next(self):
        self.click_element(type_next)

    def click_number(self, number):
        ul = self.find_elements(type_pagination)
        for now in ul:
            if now.text == str(number):
                now.click()
                break

    def input_pagination_editor(self, value, *key):
        editor = self.find_element(type_pagination_entirety)
        editor.clear()
        if key[0] != 0 and len(key) != 0:
            editor.send_keys(value, Keys.ENTER)
        elif key == 0 or len(key) == 0:
            editor.send_keys(value)

    def input_records(self, value):
        Str = str(value) + "条/页"
        self.ul_input(Str, type_records, type_records_li)