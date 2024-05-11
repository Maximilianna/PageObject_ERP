from selenium.webdriver.support.select import Select


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
