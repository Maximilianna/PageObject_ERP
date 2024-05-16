from Website.page_objects.MessagePage import MessagePage
from Website.page_elements.WareHouse import *


class WareHousePage(MessagePage):
    def Page_name(self):
        return "仓库信息"

    def input_Commissioner(self, commissioner):
        if type(commissioner) == int:
            commissioner = "CKZY" + str(commissioner)
        self.ul_input(commissioner, type_Commissioner)

    def input_PhoneNumber(self, phoneNumber):
        self.input_element(type_phoneNumber, phoneNumber)

    def input_Address(self, address):
        self.input_element(type_address, address)
