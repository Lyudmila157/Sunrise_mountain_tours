import allure
from base.base_page import BasePage
from config.links import Links
from selenium.webdriver.support import expected_conditions as EC


class RouteBaikalPage(BasePage):
    PAGE_URL = Links.ROUTE_PAGE

    BAIKAL_LINK = ("xpath", "//li[@class='active']")
    WINTER_BAIKAL_LINK = ("xpath", "(//div[@class='name'])[1]")
    PROGRAM_TRIP_LINK = ("xpath", "//div[@class='tab tour_program']")
    ELEMENT_GALOCHKA = ("xpath", "(//ul[@class='galochka'])[1]")

    @allure.step("Enter Baikal link")
    def enter_baikal_link(self):
        self.wait.until(EC.element_to_be_clickable(self.BAIKAL_LINK)).click()

    @allure.step("Enter winter Baikal link")
    def enter_winter_baikal_link(self):
        self.wait.until(EC.element_to_be_clickable(self.WINTER_BAIKAL_LINK)).click()

    @allure.step("Enter program trip link")
    def enter_program_trip_link(self):
        self.wait.until(EC.element_to_be_clickable(self.PROGRAM_TRIP_LINK)).click()

    @allure.step("Presence element")
    def presence_element(self):
        self.wait.until(EC.visibility_of_element_located(self.ELEMENT_GALOCHKA))



