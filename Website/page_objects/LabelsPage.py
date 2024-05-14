from Website.page_objects.BasePage import BasePage
from Website.page_elements.Labels import *


class LabelsPage(BasePage):
    def close_labels(self, *labelName):
        labels = self.find_elements(type_labels)
        for label in labels:
            if len(labels) < 2:
                print("标签页小于2页，无法关闭！")
                break
            if type(labelName[0]) == str and label.text == labelName[0]:
                label.find_element(type_label[0], type_label[1]).click()
                break
            elif label.text == self.Page_name():
                label.find_element(type_label[0], type_label[1]).click()
                break

    # 需要继承类重写
    def Page_name(self):
        return ""