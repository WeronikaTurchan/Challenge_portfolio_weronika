import os
import time
import unittest

from selenium import webdriver
from selenium.webdriver.chrome.service import Service

from pages.Add_a_player import AddAPlayer
from pages.dashboard import Dashboard
from pages.login_page import LoginPage
from utils.settings import DRIVER_PATH, IMPLICITLY_WAIT


class TestAddAPlayer(unittest.TestCase):
    driver = None

    @classmethod
    def setUp(self):
        os.chmod(DRIVER_PATH, 755)
        self.driver_service = Service(executable_path=DRIVER_PATH)
        self.driver = webdriver.Chrome(service=self.driver_service)
        self.driver.get('https://scouts-test.futbolkolektyw.pl/en')
        self.driver.fullscreen_window()
        self.driver.implicitly_wait(IMPLICITLY_WAIT)

    def test_login_page(self):
        user_login = LoginPage(self.driver)
        user_login.title_of_page()
        user_login.type_in_email('user05@getnada.com')
        user_login.type_in_password('Test-1234')
        user_login.click_sign_in_button()
        dashboard_page = Dashboard(self.driver)
        dashboard_page.add_player_page()
        add_player = AddAPlayer(self.driver)
        add_player.type_in_email('karol.lis@gmail.com')
        add_player.type_in_name('Karol')
        add_player.type_in_surname('Lis')
        add_player.type_in_phone('+48 243 908 111')
        add_player.type_in_weight('95')
        add_player.type_in_height('192')
        add_player.type_in_age('17.05.1999')
        time.sleep(5)

    #def test_Add_a_player(self):
     #   add_player = AddAPlayer(self.driver)
      #  add_player.type_in_name('Karol')
       # add_player.type_in_surname('Lisek')
        #time.sleep(5)

    @classmethod
    def tearDown(self):
        self.driver.quit()
