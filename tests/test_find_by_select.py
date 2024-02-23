import allure
from base.base_test import BaseTest


@allure.feature("Find by select test")
class TestFindBySelect(BaseTest):

    @allure.title("Find by select test")
    @allure.severity("Critical")
    def test_find_by_select(self):
        self.find_by_select_page.open()
        self.find_by_select_page.enter_arkhyz_link()
        self.find_by_select_page.button_on()
        self.find_by_select_page.find_by_select()
        self.find_by_select_page.enter_arrow()
        self.find_by_select_page.click_on_number_seven()
        self.find_by_select_page.button_on_two()
        self.find_by_select_page.find_by_select_next_month()
        self.find_by_select_page.click_on_twenty_three()
        self.find_by_select_page.find_by_select_region()
        self.find_by_select_page.find_by_select_type()
        self.find_by_select_page.find_by_select_home()
        self.find_by_select_page.find_by_select_type_two()
        self.find_by_select_page.find_instructors()
        self.find_by_select_page.click_on_find_button()
        self.find_by_select_page.presence_element()
