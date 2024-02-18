import pytest
from pages.route_page import RoutePage


class BaseTest:
    route_page: RoutePage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.route_page = RoutePage(driver)
