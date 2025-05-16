from base.test_base import TestBase
import random
import allure
import pytest
from selenium import webdriver


@allure.feature("Profile Functionality")
class TestFeatureProfile(TestBase):

    @allure.title("Change profile name")
    @allure.severity("Critical")
    @pytest.mark.smoke
    def test_change_profile_name(self):
        self.login_page.open()
        self.login_page.enter_login(self.data.LOGIN)
        print(self.data.LOGIN)
        self.login_page.enter_password(self.data.PASSWORD)
        print(self.data.PASSWORD)
        self.login_page.submit_button()
        driver = webdriver.Chrome()
        print(driver.current_url)
        self.dashboard_page.is_opened()
        self.dashboard_page.click_my_info_link()
        self.personal_page.change_name(f"Test{random.randint(1000, 10000)}")
        self.personal_page.save_changes()
        self.personal_page.is_changes_saved()
        self.personal_page.make_screenshot("Success")
