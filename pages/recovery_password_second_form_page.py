import time
import allure
from pages.base_page import BasePage
from locators.recovery_password_second_form_page_locators import RecoveryPasswordSecondFormPageLocators

class RecoveryPasswordSecondFormPage(BasePage):

    @allure.step('клик по кнопке скрыть и показать пароль')
    def click_on_button_show_and_hide_password(self):
        self.click_on_element(locator=RecoveryPasswordSecondFormPageLocators.button_show_and_hide_password)

    @allure.step('получение статуса кнопки ввода пароля')
    def get_status_button_input_password(self):
        return self.find_element(locator=RecoveryPasswordSecondFormPageLocators.button_input_password_after_click).get_attribute('class')

    @allure.step('получение текущего url')
    def return_current_url(self):
        return self.get_current_url(web='https://stellarburgers.nomoreparties.site/reset-password')

    @allure.step('получение атрибута кнопки ввода пароля')
    def return_attribute_input_button_password(self):
        self.find_element(locator=RecoveryPasswordSecondFormPageLocators.button_input_password)

