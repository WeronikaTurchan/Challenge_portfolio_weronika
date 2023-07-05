from pages.base_page import BasePage


class Dashboard(BasePage):
    button_xpath = "//*[@id='login']"
    Main_page = "//*[@class="MuiListItemText-root jss29 jss30"]/span"
    Players = "//*[@class="MuiListItemText-root jss29 jss31"]/span"
    Polski = "//*[@class='MuiListItemText-root']/span"
    Sign_out = "//*[text()='Sign out']"
    Add_player = //*[text()='Add player']
    Activity = "//*[text()='Activity']"
    Scouts_panel = "//*[text()='Scouts Panel']"
    Shortcuts = "//*[text()='Shortcuts']"
    Players_count = "//*[text()='Players count']"
    Events_count = "//*[text()='Events count']"
    Description = "//*[@class="MuiTypography-root MuiTypography-body2 MuiTypography-colorTextSecondary"]"

    pass
