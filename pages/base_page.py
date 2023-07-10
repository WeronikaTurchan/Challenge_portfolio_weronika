from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver


class BasePage():

    def __init__(self, driver: WebDriver):
        """

        :rtype: object
        """
        self.driver = driver

    def field_send_keys(self, selector: object, value: object, locator_type: object = By.XPATH) -> object:
        return self.driver.find_element(locator_type, selector).send_keys(value)
    #def field_send_password(self, selector: object, value: object, locator_type: object =By.XPATH):
     #   return self.driver.find_element(locator_type, selector).send_password(value)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()
