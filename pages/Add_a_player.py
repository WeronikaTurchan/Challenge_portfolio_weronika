import time
from pages.base_page import BasePage


class AddAPlayer (BasePage):
    Email_xpath = "//*[@name='email']"
    Name_xpath = "//*[@name='name']"
    Surname_xpath = "//*[@name='surname']"
    Phone_xpath = "//*[@name='phone']"
    Weight_xpath = "//*[@name='weight']"
    Height_xpath = "//*[@name='height']"
    Age_xpath = "//*[@name='age']"
    Leg_xpath = "//*[@id='mui-component-select-leg']"
    Right_leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[1]"
    Left_Leg_xpath = "//*[@id='menu-leg']/div[3]/ul/li[2]"
    Club_xpath = "//*[@name='club']"
    Main_position_xpath = "//*[@name='mainPosition']"
    District_xpath = "//*[@id='mui-component-select-district']"
    Opole_xpath = "//*[@id='menu-district']/div[3]/ul/li[8]"
    Achievements_xpath = "//*[@name='achievements']"
    Add_language_xpath = "//*[text()='Add language']"
    Enter_language_xpath = "//*/div[15]/div/div/div/input"
    Submit_button_xpath = "//*/div[3]/button[1]/span[1]"
    Clear_button_xpath = "//*/button[2]/span[1]"

    def type_in_email(self, email):
        self.field_send_keys(self.Email_xpath, email)

    def type_in_name(self, name):
        self.field_send_keys(self.Name_xpath, name)

    def type_in_surname(self, surname):
        self.field_send_keys(self.Surname_xpath, surname)

    def type_in_phone(self, phone):
        self.field_send_keys(self.Phone_xpath, phone)

    def type_in_weight(self, weight):
        self.field_send_keys(self.Weight_xpath, weight)

    def type_in_height(self, height):
        self.field_send_keys(self.Height_xpath, height)

    def type_in_age(self, age):
        self.field_send_keys(self.Age_xpath, age)

    def type_in_leg(self):
        self.click_on_the_element(self.Leg_xpath)
        self.click_on_the_element(self.Left_Leg_xpath)

    def type_in_club(self, club):
        self.field_send_keys(self.Club_xpath, club)

    def type_in_position(self, position):
        self.field_send_keys(self.Main_position_xpath, position)

    def type_in_district(self):
        self.click_on_the_element(self.District_xpath)
        self.click_on_the_element(self.Opole_xpath)

    def type_in_achievements(self, achievements):
        self.field_send_keys(self.Achievements_xpath, achievements)

    def type_in_language(self, language):
        self.click_on_the_element(self.Add_language_xpath)
        self.field_send_keys(self.Enter_language_xpath, language)

    def submit_add_player(self):
        self.click_on_the_element(self.Submit_button_xpath)
    time.sleep(5)

