import allure
from base.base_test import BaseTest


@allure.feature("Choose route Dagestan test")
class TestRouteDagestan(BaseTest):

    @allure.title("Route Dagestan test")
    @allure.severity("Critical")
    def test_choose_dagestan_route(self):
        self.route_dagestan_page.open()
        self.route_dagestan_page.enter_dagestan_button()
        self.route_dagestan_page.enter_select_enter()
        self.route_dagestan_page.enter_date_click()
        # self.route_dagestan_page.find_by_select()
        self.route_dagestan_page.enter_on_trekking_link()
        self.route_dagestan_page.submit_an_application()
        self.route_dagestan_page.presence_element_one()
        self.route_dagestan_page.presence_element_two()
        # self.route_dagestan_page.find_by_select_date()
        self.route_dagestan_page.enter_on_select_date_enter()
        self.route_dagestan_page.date_in_select_enter()
        self.route_dagestan_page.enter_radio()
        self.route_dagestan_page.enter_name_on_personal_link()
        self.route_dagestan_page.enter_on_birthday_link()
        self.route_dagestan_page.click_on_radio_woman()
        self.route_dagestan_page.enter_on_telephone_link()
        self.route_dagestan_page.enter_email_button()
        self.route_dagestan_page.enter_town_button()
        self.route_dagestan_page.enter_on_radio_meal()
        self.route_dagestan_page.comments()
        self.route_dagestan_page.click_on_radio_yes()

