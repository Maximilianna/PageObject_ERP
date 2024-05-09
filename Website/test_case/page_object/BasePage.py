from selenium.webdriver.support.select import Select


class BasePage(object):
    def __init__(self, driver):
        self.driver = driver

    def open(self, url):
        self.driver.get(url)

    def find_element(self, type, name):
        return self.driver.find_element(type, name)

    def find_elements(self, type, name):
        return self.driver.find_elements(type, name)

    def click_element(self, type, name):
        self.find_element(type, name).click()

    def input_element(self, type, name, value):
        self.find_element(type, name).send_keys(value)

    def select_element(self, type, name, str):
        Select(self.find_element(type, name)).select_by_visible_text(str)
