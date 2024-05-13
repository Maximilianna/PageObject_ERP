from Website.page_objects.LabelsPage import LabelsPage
from time import sleep
from Website.page_elements.Base import *
import traceback


class ManageDataPage(LabelsPage):
    def ul_input(self, str, input, ul):
        self.click_element(input)
        sleep(0.5)
        ul = self.find_elements(ul)
        try:
            for now in ul:
                if now.get_attribute("textContent") == str:
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

    def click_number(self, number):
        ul = self.find_elements(type_pagination)
        for now in ul:
            if now.text == str(number):
                now.click()
                break