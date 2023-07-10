import os
import time
import unittest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestLoginPage(unittest.TestCase):

    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_logowania(self):
        user_login = LoginPage(self.driver)

    def test_log_in_the_system(self):
        user_login = LoginPage(self.driver)
        user_login.type_in_email('user05@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
