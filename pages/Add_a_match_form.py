from pages.base_page import BasePage


class AddAMatchForm (BasePage):

Date_xpath = "//*[@name='date']"
CheckBox_xpath = "//*[@class='MuiFormGroup-root']"
CheckBox_circle_xpath = "//*[@class='MuiIconButton-label']/div"
Submit_button_xpath = "//*[@class='MuiCardActions-root MuiCardActions-spacing']/button[1]"
Clear_button_xpath = "//*[contains(@class, 'MuiButton-containedSecondary')]"
Matches_xpath = "//*/ul[2]/div[2]/div[2]/span"
My_team_xpath = "//*[text()='My team']"
Enemy_team_xpath = "//*[text()='Enemy team']"
Time_Played_xpath = "//*[text()='Time played']"
Tshirt_color_xpath = "//*[@name='tshirt']"
pass
