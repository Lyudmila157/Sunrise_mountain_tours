import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC
# from selenium.webdriver.support.select import Select
from selenium.webdriver import Keys

class RouteDagestanPage(BasePage):
    PAGE_URL = Links.ROUTE_PAGE

    DAGESTAN_TOUR_MAIN = ("xpath", "(//li/a)[31]")
    SELECT_ENTER = ("xpath", "(//div[@class='select-pick'])[2]")
    DATE_CLICK = ("xpath", "//li[@rel='2398']")
    # SELECT = ("xpath", "(//select[@class='vosh-dropdown select-hidden'])[1]")
    TREKKING = ("xpath", "(//div[@class='name'])[2]")
    SUBMIT_APPLICATION = ("xpath", "//div[@class='tab order']")
    NAME_PRESENT_ONE = ("xpath", "(//span[@class='ui-selectmenu-text'])[1]")
    NAME_PRESENT_TWO = ("xpath", "(//span[@class='ui-selectmenu-text'])[2]")
    # SELECT_TWO = ("xpath", "//select[@class='sel-ui sel-ui-date']")
    SELECT_DATE_ENTER = ("xpath", "(//span[@class='ui-icon ui-icon-triangle-1-s'])[3]")
    DATE_IN_SELECT = ("xpath", "(//li[@class='ui-menu-item'])[3]")
    # RADIO = ("xpath", "(//input[@type='radio'])[1]")
    RADIO_ACTION = ("xpath", "//label[@for='go-alone']")
    PERSONAL_LINK = ("xpath", "(//input[@id='in-name'])[1]")
    BIRTHDAY_LINK = ("xpath", "(//input[@id='in-birthday'])[1]")
    RADIO_WOMAN = ("xpath", "//label[@for='sex-1-2']")
    TELEPHONE_LINK = ("xpath", "(//input[@id='in-phone'])[1]")
    EMAIL_BUTTON = ("xpath", "(//input[@id='in-email'])[1]")
    TOWN_BUTTON = ("xpath", "(//input[@id='in-placeresidence'])[1]")
    RADIO_MEAL = ("xpath", "//label[@for='type-food-1-1']")
    COMMENTS = ("xpath", "//textarea[@id='in-text']")
    RADIO_YES = ("xpath", "//label[@for='personal-data-processing']")

    @allure.step("Enter dagestan tour main")
    def enter_dagestan_button(self):
        self.wait.until(EC.element_to_be_clickable(self.DAGESTAN_TOUR_MAIN)).click()

    @allure.step("Enter select enter")
    def enter_select_enter(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_ENTER)).click()

    @allure.step("Enter date click")
    def enter_date_click(self):
        self.wait.until(EC.element_to_be_clickable(self.DATE_CLICK)).click()

    # @allure.step("Find by select")
    # def find_by_select(self):
    #     dropdown = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT)))
    #     dropdown.select_by_value("2106")

    @allure.step("Enter on trekking link")
    def enter_on_trekking_link(self):
        self.wait.until(EC.element_to_be_clickable(self.TREKKING)).click()

    @allure.step("Enter on submit an application")
    def submit_an_application(self):
        self.wait.until(EC.element_to_be_clickable(self.SUBMIT_APPLICATION)).click()

    @allure.step("Presence element_one")
    def presence_element_one(self):
        self.wait.until(EC.visibility_of_element_located(self.NAME_PRESENT_ONE))

    @allure.step("Presence element_two")
    def presence_element_two(self):
        self.wait.until(EC.visibility_of_element_located(self.NAME_PRESENT_TWO))

    @allure.step("Enter on select date enter")
    def enter_on_select_date_enter(self):
        self.wait.until(EC.element_to_be_clickable(self.SELECT_DATE_ENTER)).click()

    @allure.step("Date in select enter")
    def date_in_select_enter(self):
        self.wait.until(EC.element_to_be_clickable(self.DATE_IN_SELECT)).click()

    # @allure.step("Find by select date")
    # def find_by_select_date(self):
    #     dropdown_two = Select(self.wait.until(EC.visibility_of_element_located(self.SELECT_TWO)))
    #     dropdown_two.select_by_value("2398")

    @allure.step("Enter radio")
    def enter_radio(self):
        self.wait.until(EC.visibility_of_element_located(self.RADIO_ACTION)).click()

    @allure.step("Enter name on personal link")
    def enter_name_on_personal_link(self):
        self.wait.until(EC.element_to_be_clickable(self.PERSONAL_LINK)).send_keys("Иванов Иван Иванович")

    @allure.step("Enter on birthday link")
    def enter_on_birthday_link(self):
        self.wait.until(EC.visibility_of_element_located(self.BIRTHDAY_LINK)).send_keys("05.07.1990")

    @allure.step("Click on radio woman")
    def click_on_radio_woman(self):
        self.wait.until(EC.element_to_be_clickable(self.RADIO_WOMAN)).click()

    @allure.step("Enter on telephone link")
    def enter_on_telephone_link(self):
        self.wait.until(EC.visibility_of_element_located(self.TELEPHONE_LINK)).send_keys("939) 377-77-77")

    @allure.step("Enter email button")
    def enter_email_button(self):
        self.wait.until(EC.visibility_of_element_located(self.EMAIL_BUTTON)).send_keys("test@yandex.ru")

    @allure.step("Enter town button")
    def enter_town_button(self):
        self.wait.until(EC.visibility_of_element_located(self.TOWN_BUTTON)).send_keys("Москва")

    @allure.step("Enter on radio meal")
    def enter_on_radio_meal(self):
        self.wait.until(EC.element_to_be_clickable(self.RADIO_MEAL)).click()

    @allure.step("Comments")
    def comments(self):
        self.wait.until(EC.visibility_of_element_located(self.COMMENTS)).send_keys("ТЕСТ")

    @allure.step("Click on radio yes")
    def click_on_radio_yes(self):
        self.wait.until(EC.element_to_be_clickable(self.RADIO_YES)).click()





