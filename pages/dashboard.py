import time
from pages.base_page import BasePage
from pages.login_page import LoginPage


class Dashboard(BasePage):
    button_xpath = "//*[@id='login']"
    Main_page_xpath = "//*[@class='MuiListItemText-root jss29 jss30']/span"
    Players_xpath = "//*/ul[1]/div[2]/div[2]/span"
    Language_xpath = "//*[@class='MuiListItemText-root']/span"
    Sign_out_xpath = "//*[text()='Sign out']"
    Add_player_xpath = "//*[text()='Add player']"
    Activity_xpath = "//*[text()='Activity']"
    Scouts_panel_xpath = "//*[text()='Scouts Panel']"
    Shortcuts_xpath = "//*[text()='Shortcuts']"
    Players_count_xpath = "//*[text()='Players count']"
    Events_count_xpath = "//*[text()='Events count']"
    Description_xpath = "//*[@class='MuiTypography-root MuiTypography-body2 MuiTypography-colorTextSecondary']"
    expected_title = "Scouts panel"
    dashboard_url = 'https://scouts-test.futbolkolektyw.pl/en'
    add_player_url = 'https://scouts-test.futbolkolektyw.pl/en/players/add'
    add_player_expected_title = "Add player"
    language_url = 'https://scouts-test.futbolkolektyw.pl/en'
    expected_language = "Polski"
    players_url = 'https://scouts-test.futbolkolektyw.pl/en/players'
    players_expected_title = 'Players'

    def title_of_page(self):
        self.wait_for_element_to_be_clicable(self.button_xpath)
        assert self.get_page_title(self.dashboard_url) == self.expected_title

    def add_player_page(self):
        self.click_on_the_element(self.Add_player_xpath)
        time.sleep(3)
        assert self.get_page_title(self.add_player_url) == self.add_player_expected_title

    def players(self):
        self.click_on_the_element(self.Players_xpath)
        time.sleep(5)
        assert self.get_page_title(self.players_url) == self.players_expected_title

    def language(self):
        self.click_on_the_element(self.Language_xpath)

