from Driver.driver import get_driver
from unittest import TestCase


class TestMyUnit(TestCase):
    def setUp(self):
        self.driver = get_driver()
        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def tearDown(self):
        self.driver.quit()