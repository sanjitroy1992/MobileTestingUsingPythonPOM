from appium import webdriver
import unittest
import HtmlTestRunner
from PageObjects.LoginPage import LoginPage
from PageObjects.HomePage import HomePage
from Resources.TestData import TestData
from Resources.Locators import Locators


class Search_Item(unittest.TestCase):

    @classmethod
    def setUp(cls):
        cls.driver = webdriver.Remote(command_executor=TestData.host, desired_capabilities=TestData.desired_cap)
        cls.driver.implicitly_wait(10)

    def test_01_search_product(self):
        driver = self.driver
        login = LoginPage(driver)
        login.skip_sign_in()
        home_page = HomePage(driver)
        home_page.search_item(TestData.search_item_text)
        home_page.select_item(Locators.item_xpath)
        home_page.use_pin_code()
        home_page.enter_pin_code(TestData.pin_code)
        home_page.apply_pin_code()

    @classmethod
    def tearDown(cls):
        cls.driver.close_app()
        print("Test Completed")

if __name__=='__main__':
    unittest.main(testRunner=HtmlTestRunner.HTMLTestRunner(output=TestData.HTML_Report_Path))