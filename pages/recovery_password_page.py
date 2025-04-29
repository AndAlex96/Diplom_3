from locators.recovery_password_page_locators import RecoveryPasswordPageLocators
from pages.base_page import BasePage
import allure

class RecoveryPasswordPage(BasePage):

    @allure.step('ввод email')
    def send_email(self, text):
        self.input_text(locator=RecoveryPasswordPageLocators.input_email, text=text)

    @allure.step('клик по кнопке восстановить')
    def click_on_button_recovery(self):
        self.click_on_element(locator=RecoveryPasswordPageLocators.button_recovery)

    @allure.step('получение текущего url')
    def return_current_url(self):
        return self.get_current_url(web='https://stellarburgers.nomoreparties.site/forgot-password')