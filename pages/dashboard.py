from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*[@id='login']"
    Main_page_xpath = "//*[@class="MuiListItemText-root jss29 jss30"]/span"
    Players_xpath = "//*[@class="MuiListItemText-root jss29 jss31"]/span"
    Language_xpath = "//*[@class='MuiListItemText-root']/span"
    Sign_out_xpath = "//*[text()='Sign out']"
    Add_player_xpath = //*[text()='Add player']
    Activity_xpath = "//*[text()='Activity']"
    Scouts_panel_xpath = "//*[text()='Scouts Panel']"
    Shortcuts_xpath = "//*[text()='Shortcuts']"
    Players_count_xpath = "//*[text()='Players count']"
    Events_count_xpath = "//*[text()='Events count']"
    Description_xpath = "//*[@class="MuiTypography-root MuiTypography-body2 MuiTypography-colorTextSecondary"]"

    pass
