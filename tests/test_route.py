import allure
from base.base_test import BaseTest

@allure.feature("Choose route test")
class TestRoute(BaseTest):

    @allure.title("Route test")
    @allure.severity("Critical")
    def test_choose_route(self):
        self.route_page.open()
        self.route_page.enter_route_button()
        self.route_page.enter_arkhyz_tour_main()
        # self.route_page.select_locator_arkhyz()
        self.route_page.enter_hiking_tour()
        self.route_page.enter_mountain_camp()
        self.route_page.enter_information_place()
        self.route_page.enter_comparison_table()
        self.route_page.click_on_difficulty_level()
        self.route_page.presence_element()




