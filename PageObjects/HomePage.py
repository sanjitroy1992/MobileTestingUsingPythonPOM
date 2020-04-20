from Resources.Locators import Locators
from appium.webdriver.extensions.android.nativekey import AndroidKey
from Resources.TestData import TestData

class HomePage:

    def __init__(self, driver):
        self.driver = driver
        self.search_bar_id = Locators.search_bar_id
        self.item_xpath = Locators.item_xpath
        self.use_pin_code_xpath = Locators.use_pin_code_xpath
        self.pin_code_xpath = Locators.pin_code_xpath
        self.apply_button_xpath = Locators.apply_button_xpath

    def search_item(self, item_to_search):
        search_bar = self.driver.find_element_by_id(Locators.search_bar_id)
        search_bar.click()
        search_bar.send_keys(item_to_search)
        self.driver.press_keycode(AndroidKey.ENTER)

    def select_item(self, item_element_locator):
        self.driver.find_element_by_xpath(item_element_locator).click()

    def use_pin_code(self):
        self.driver.find_element_by_xpath(self.use_pin_code_xpath).click()

    def enter_pin_code(self, pin_code_text):
        pin_code = self.driver.find_element_by_xpath(self.pin_code_xpath)
        pin_code.click()
        pin_code.clear()
        pin_code.send_keys(pin_code_text)
        self.driver.press_keycode(AndroidKey.ENTER)

    def apply_pin_code(self):
        self.driver.find_element_by_xpath(self.apply_button_xpath).click()

