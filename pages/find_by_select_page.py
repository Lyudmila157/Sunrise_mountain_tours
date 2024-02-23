import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.select import Select


class FindBySelect(BasePage):
    PAGE_URL = Links.ROUTE_PAGE

    ARKHYZ_LINK = ("xpath", "(//ul/li/a)[25]")
    BUTTON_ON = ("xpath", "(//button[@type='button'])[3]")
    SELECT_MOUNTH = ("xpath", "//select[@class='ui-datepicker-month']")
    ARROW = ("xpath", "//span[@class='ui-icon ui-icon-circle-triangle-e']")
    NUMBER_SEVEN = ("xpath", "(//a[@class='ui-state-default'])[7]")
    BUTTON_ON_TWO = ("xpath", "(//button[@type='button'])[4]")
    NUMBER_TWENTY_THREE = ("xpath", "(//td[@class=' ui-datepicker-week-end '])[15]")
    SELECT_REGION = ("xpath", "//select[@name='region']")
    SELECT_TYPE = ("xpath", "//select[@name='type_rest']")
    SELECT_HOME = ("xpath", "//select[@name='accommodation']")
    SELECT_TYPE_TWO = ("xpath", "//select[@name='type']")
    SELECT_INSTRUCTORS = ("xpath", "//select[@name='instructors']")
    FIND_BUTTON = ("xpath", "(//button[@type='submit'])[1]")
    SIBIR_NAME = ("xpath", "(//div[@class='name'])[1]")

    @allure.step("Enter Arkhyz link")
    def enter_arkhyz_link(self):
        self.wait.until(EC.element_to_be_clickable(self.ARKHYZ_LINK)).click()

    @allure.step("Button on")
    def button_on(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ON)).click()

    @allure.step("Find by select")
    def find_by_select(self):
        dropdown = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_MOUNTH)))
        dropdown.select_by_value("3")

    @allure.step("Enter arrow")
    def enter_arrow(self):
        self.wait.until(EC.element_to_be_clickable(self.ARROW)).click()

    @allure.step("Click on number seven")
    def click_on_number_seven(self):
        self.wait.until(EC.element_to_be_clickable(self.NUMBER_SEVEN)).click()

    @allure.step("Button on two")
    def button_on_two(self):
        self.wait.until(EC.element_to_be_clickable(self.BUTTON_ON_TWO)).click()

    @allure.step("Find by select next month")
    def find_by_select_next_month(self):
        dropdown = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_MOUNTH)))
        dropdown.select_by_value("5")

    @allure.step("Click on twenty three")
    def click_on_twenty_three(self):
        self.wait.until(EC.element_to_be_clickable(self.NUMBER_TWENTY_THREE)).click()

    @allure.step("Find by select region")
    def find_by_select_region(self):
        dropdown_two = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_REGION)))
        dropdown_two.select_by_value("25")

    @allure.step("Find by select type")
    def find_by_select_type(self):
        dropdown_three = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_TYPE)))
        dropdown_three.select_by_value("1")

    @allure.step("Find by select home")
    def find_by_select_home(self):
        dropdown_four = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_HOME)))
        dropdown_four.select_by_value("2")

    @allure.step("Find by select type two")
    def find_by_select_type_two(self):
        dropdown_five = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_TYPE_TWO)))
        dropdown_five.select_by_value("2")

    @allure.step("Find instructors")
    def find_instructors(self):
        dropdown_six = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_INSTRUCTORS)))
        dropdown_six.select_by_value("7")

    @allure.step("Click on find button")
    def click_on_find_button(self):
        self.wait.until(EC.element_to_be_clickable(self.FIND_BUTTON)).click()

    @allure.step("Presence element")
    def presence_element(self):
        self.wait.until(EC.visibility_of_element_located(self.SIBIR_NAME))
