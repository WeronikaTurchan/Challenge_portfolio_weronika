# import email
import time

from selenium.webdriver.chrome.webdriver import WebDriver

from pages.base_page import BasePage


class LoginPage(BasePage):
    login_field_xpath = "//*[@id='login']"
    password_field_xpath = "//*[@id='password']"
    sign_in_button_xpath = "//span[1]"
    login_url = ('https://scouts-test.futbolkolektyw.pl/en')
    expected_title = "Scouts panel - sign in"
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_player_expected_title = "Add Player"

    def type_in_email(self, email):
        self.field_send_keys(self.login_field_xpath, email)

    def type_in_password(self, password):
        self.field_send_keys(self.password_field_xpath, password)

    def click_sign_in_button(self):
        self.click_on_the_element(self.sign_in_button_xpath)

    def title_of_page(self):
        time.sleep(5)
        assert self.get_page_title(self.login_url) == self.expected_title

    #def add_player_page(self):
     #   self.click_on_the_element(self.Add_player_xpath)
      #  assert self.get_page_title(self.add_player_url) == self.add_player_expected_title
