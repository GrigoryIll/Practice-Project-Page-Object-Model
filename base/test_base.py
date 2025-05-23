import pytest
from pages.dashboard_page import DashboardPage
from pages.login_page import LoginPage
from pages.personal_page import PersonalPage
from config.data import Data


class TestBase:

    data: Data
    login_page: LoginPage
    dashboard_page: DashboardPage
    personal_page: PersonalPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.login_page = LoginPage(driver)
        request.cls.dashboard_page = DashboardPage(driver)
        request.cls.personal_page = PersonalPage(driver)
        request.cls.data = Data()
