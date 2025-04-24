import time
import allure
from pages.base_page import BasePage
from locators.personal_user_profile_page_locators import PersonalUserProfilePageLocators

class PersonalUserProfilePage(BasePage):

    @allure.step('клик по кнопке история заказов')
    def click_on_button_orders_history(self):
        time.sleep(1)
        self.click_on_element(locator=PersonalUserProfilePageLocators.button_order_history)

    @allure.step('клик по кнопке выход')
    def click_on_button_exit(self):
        time.sleep(1)
        self.click_on_element(locator=PersonalUserProfilePageLocators.button_exit)

    @allure.step('получение текущего url')
    def get_current_url_on_user_page(self):
        time.sleep(1)
        return self.get_current_url()

    @allure.step('получение номера последнего заказа')
    def get_number_last_order(self):
        self.scroll_to_element(locator=PersonalUserProfilePageLocators.last_order)
        return self.find_element(locator=PersonalUserProfilePageLocators.last_order).text
