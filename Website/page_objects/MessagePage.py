from Website.page_objects.LabelsPage import LabelsPage
from selenium.webdriver.common.keys import Keys
from time import sleep
from Website.page_elements.Message import *
import traceback


class MessagePage(LabelsPage):
    def click_new(self):
        self.click_element(type_new)

    def click_query(self):
        self.click_element(type_query)

    def click_reset(self):
        self.click_element(type_reset)

    def ul_input(self, Options, Input_Location, Li_Location):
        self.click_element(Input_Location)
        sleep(0.5)
        li = self.find_elements(Li_Location)
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

    def click_prev(self):
        self.click_element(type_prev)

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
        self.ul_input(Str, type_records, type_li)

    def click_data_modify(self, index):
        type_data_modify[1] = type_data_modify[1].replace("nth-child( )", f"nth-child({index})")
        self.click_element(type_data_modify)

    def click_data_switch(self, index):
        type_data_switch[1] = type_data_switch[1].replace("nth-child( )", f"nth-child({index})")
        self.click_element(type_data_switch)

    def data_switch_accept(self):
        self.alert_accept()

    def data_switch_dismiss(self):
        self.alert_dismiss()

    def click_save(self):
        self.click_element(type_save_button)

    def click_cancel(self):
        self.click_element(type_cancel_button)

    def input_add_name(self, Name):
        self.input_element(type_name, Name)

    def input_modify_name(self, Name):
        self.find_element(type_name).clear()
        self.input_add_name(Name)

    def into_page(self):
        type_into_page[1] = self.Page_name()
        self.click_element(type_into_page)

    def input_query_name(self, Name):
        self.input_element(type_query_name, Name)

    def input_query_status(self, Option):
        self.ul_input(Option, type_query_status, type_li)
