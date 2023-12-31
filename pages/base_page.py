import time

from selenium.webdriver.common.by import By
from selenium.webdriver.remote.webdriver import WebDriver
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.wait import WebDriverWait

from utils.settings import DEFAULT_LOCATOR_TYPE


class BasePage():

    def __init__(self, driver: WebDriver) -> object:
        """

        :rtype: object
        """
        self.driver = driver

    def field_send_keys(self, selector: object, value: object, locator_type: object = By.XPATH) -> object:
        return self.driver.find_element(locator_type, selector).send_keys(value)
    time.sleep(5)

    def click_on_the_element(self, selector, selector_type=By.XPATH):
        return self.driver.find_element(selector_type, selector).click()
    time.sleep(5)

    def get_page_title(self, url):
        self.driver.get(url)
        return self.driver.title

    #def assert_element_text(self, driver, xpath, expected_text):
     #   element = driver.find_element(by=By.XPATH, value=xpath)
      #  element_text = element.text
       # assert expected_text == element_text

    @classmethod
    def setUp(cls, self):
        pass

    def wait_for_element_to_be_clicable(self, locator, locator_type=DEFAULT_LOCATOR_TYPE):
        wait = WebDriverWait(self.driver, 10)
        element = wait.until(EC.element_to_be_clickable((locator_type, locator)))
        time.sleep(3)

    def assert_element_text(self, driver, param, param1):
        pass
