from pages.base_page import BasePage


class AddAPlayer (BasePage):
    Email_xpath = "//*[@name='email']"
    Name_xpath = "//*[@name='name']"
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


