import allure
from base.base_test import BaseTest


@allure.feature("Choose route Baikal test")
class TestRouteBaikal(BaseTest):

    @allure.title("Route Baikal test")
    @allure.severity("Critical")
    def test_choose_baikal_route(self):
        self.route_baikal_page.open()
        self.route_baikal_page.enter_baikal_link()
        self.route_baikal_page.enter_winter_baikal_link()
        self.route_baikal_page.enter_program_trip_link()
        self.route_baikal_page.presence_element()

