from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
import allure
from selenium.webdriver.common.keys import Keys


class PersonalPage(BasePage):

    PAGE_URL = Links.PERSONAL_PAGE
    FIRST_NAME_FIELD = ("xpath", "//input[@name='firstName']")
    SAVE_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SPINNER = ("xpath", "//div[@class='oxd-loading-spinner']")

    def change_name(self, new_name):
        with allure.step(f"Change name on '{new_name}'"):
            first_name_field = self.wait.until(
                EC.element_to_be_clickable(self.FIRST_NAME_FIELD))
            first_name_field.send_keys(Keys.CONTROL + "a")
            first_name_field.send_keys(Keys.DELETE)
            first_name_field.send_keys(new_name)
            self.name = new_name

    @allure.step("Save changes")
    def save_changes(self):
        self.wait.until(EC.element_to_be_clickable(self.SAVE_BUTTON)).click()

    @allure.step("Saved successfully")
    def is_changes_saved(self):
        self.wait.until(EC.visibility_of_all_elements_located
                        (self.FIRST_NAME_FIELD))
        self.wait.until(EC.text_to_be_present_in_element_value(
            self.FIRST_NAME_FIELD, self.name))
