import time
import allure
from locators.login_page_locators import LoginPageLocators
from pages.base_page import BasePage

class LoginPage(BasePage):

    @allure.step('Клип по кнопке восстановления пароля')
    def click_on_button_recovery_password(self):
        self.click_on_element(locator = LoginPageLocators.button_password_recovery)

    @allure.step('возвращение текущего url')
    def return_current_url(self):
        return self.get_current_url('https://stellarburgers.nomoreparties.site/login')

    @allure.step('заполнение поля email')
    def filling_in_the_email_field(self, text):
        self.input_text(locator=LoginPageLocators.input_email, text=text)

    @allure.step('заполнения поля пароль')
    def filling_in_the_password_field(self, text):
        self.input_text(locator=LoginPageLocators.input_password, text=text)

    @allure.step('клик по кнопке войти')
    def click_on_login_button(self):
        self.click_on_element(locator=LoginPageLocators.button_login)

    @allure.step('Ожидание смены адреса страницы')
    def wait_current_url(self):
        self.wait_url('https://stellarburgers.nomoreparties.site/login')