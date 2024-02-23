import pytest
from pages.route_page import RoutePage
from pages.route_baikal_page import RouteBaikalPage
from pages.find_by_select_page import FindBySelect
from pages.route_dagestan_page import RouteDagestanPage


class BaseTest:
    route_page: RoutePage
    route_baikal_page: RouteBaikalPage
    find_by_select_page: FindBySelect
    route_dagestan_page: RouteDagestanPage

    @pytest.fixture(autouse=True)
    def setup(self, request, driver):
        request.cls.driver = driver
        request.cls.route_page = RoutePage(driver)
        request.cls.route_baikal_page = RouteBaikalPage(driver)
        request.cls.find_by_select_page = FindBySelect(driver)
        request.cls.route_dagestan_page = RouteDagestanPage(driver)
