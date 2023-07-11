from pages.base_page import BasePage


class AddAPlayer (BasePage):
    Email_xpath = "//*[text()='E-mail']"
    Name_xpath = "//*/div[2]/div/label"
    Surname_xpath = "//*[@name='surname']"
    Phone_xpath = "//*[@name='phone']"
    Weight_xpath = "//*[@name='weight']"
    Height_xpath = "//*[@name='height']"
    Age_xpath = "//*[@type='date']"
    Leg_xpath = "//*[@id='mui-component-select-leg']"
    Club_xpath = "//*[@name='club']"
    Main_position_xpath = "//*[@name='mainPosition']"
    District_xpath = "//*[@id='mui-component-select-district']"
    Add_language_xpath = "//*[text()='Add language']"
    Submit_button_xpath = "//*/div[3]/button[1]/span[1]"
    Clear_button_xpath = "//*/button[2]/span[1]"
    pass