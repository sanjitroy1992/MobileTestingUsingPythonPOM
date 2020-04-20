from Resources.Locators import Locators


class LoginPage:

    def __init__(self, driver):
        self.driver = driver
        self.skip_sign_in_button_id = Locators.skip_sign_in_button_id

    def skip_sign_in(self):
        self.driver.find_element_by_id(self.skip_sign_in_button_id).click()
