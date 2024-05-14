from selenium.webdriver.support.select import Select


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, type):
        return self.driver.find_element(type[0], type[1])

    def find_elements(self, type):
        return self.driver.find_elements(type[0], type[1])

    def click_element(self, type):
        self.find_element(type).click()

    def click_elements(self, type, index):
        self.find_elements(type)[index].click()

    def input_element(self, type, value):
        self.find_element(type).send_keys(value)

    def input_elements(self, type, value, index):
        self.find_elements(type)[index].send_keys(value)

    def select_element(self, type, My_str):
        Select(self.find_element(type)).select_by_visible_text(My_str)

    def alert_accept(self):
        self.driver.switch_to.alert.accept()

    def alert_dismiss(self):
        self.driver.switch_to.alert.dismiss()
