import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select


class RoutePage(BasePage):
    PAGE_URL = Links.HOST

    ROUTE_BUTTON = ("xpath", "(//li/a)[7]")
    ARKHYZ_TOUR_MAIN = ("xpath", "(//div/ul/li/a)[17]")
    SELECT_LOCATOR_ARKHYZ = ("xpath", "(//select[@class='vosh-dropdown select-hidden'])[4]")
    HIKING_TOUR = ("xpath", "(//div[@class='name'])[14]")
    MOUNTAIN_CAMP = ("xpath", "(//ul/li/a[@target='_blank'])[1]")
    INFORMATION_PLACE = ("xpath", "//div[@class='tab information_about']")
    COMPARISON_TABLE = ("xpath", "(//div/p/a)[4]")
    DIFFICULTY_LEVEL = ("xpath", "(//a[@target='_blank'])[5]")
    PRESENCE_ELEMENT = ("xpath", "(//div[@class='title'])[5]")

    @allure.step("Enter route button")
    def enter_route_button(self):
        self.wait.until(EC.element_to_be_clickable(self.ROUTE_BUTTON)).click()

    @allure.step("Enter arkhyz tour main")
    def enter_arkhyz_tour_main(self):
        self.wait.until(EC.visibility_of_element_located(self.ARKHYZ_TOUR_MAIN)).click()

    # @allure.step("Choose select locator arkhyz")
    # def select_locator_arkhyz(self):
    #     Select(self.wait.until(EC.presence_of_element_located(self.SELECT_LOCATOR_ARKHYZ))).select_by_value("2287")

    @allure.step("Hiking tour")
    def enter_hiking_tour(self):
        self.wait.until(EC.element_to_be_clickable(self.HIKING_TOUR)).click()

    @allure.step("Mountain camp")
    def enter_mountain_camp(self):
        self.wait.until(EC.element_to_be_clickable(self.MOUNTAIN_CAMP)).click()

    @allure.step("Information place")
    def enter_information_place(self):
        self.wait.until(EC.element_to_be_clickable(self.INFORMATION_PLACE)).click()

    @allure.step("Comparison table")
    def enter_comparison_table(self):
        self.wait.until(EC.element_to_be_clickable(self.COMPARISON_TABLE)).click()

    @allure.step("Click on difficulty level")
    def click_on_difficulty_level(self):
        self.wait.until(EC.element_to_be_clickable(self.DIFFICULTY_LEVEL)).click()

    @allure.step("Presence element")
    def presence_element(self):
        self.wait.until(EC.visibility_of_element_located(self.PRESENCE_ELEMENT))
















