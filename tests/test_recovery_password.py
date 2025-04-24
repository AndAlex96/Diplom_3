from pages.recovery_password_second_form_page import RecoveryPasswordSecondFormPage
from pages.login_page import LoginPage
from pages.recovery_password_page import RecoveryPasswordPage
from pages.start_page import StartPage
from conftest import driver
from helpers.auxiliary_functions_for_api import generate_email_password_name
import allure

class TestRecoveryPassword:

    @allure.title('переход на страницу восстановления пароля по кнопке «Восстановить пароль»')
    def test_go_to_the_password_recovery_page(self, driver):
        start_page = StartPage(driver)
        login_page = LoginPage(driver)

        start_page.click_on_button_personal_account()
        login_page.click_on_button_recovery_password()

        assert login_page.return_current_url() == 'https://stellarburgers.nomoreparties.site/forgot-password'

    @allure.title('ввод почты и клик по кнопке «Восстановить»')
    def test_send_email_and_click_button_recovery(self, driver):
        start_page = StartPage(driver)
        login_page = LoginPage(driver)
        recovery_pas_page = RecoveryPasswordPage(driver)
        recovery_pas_page_s_f = RecoveryPasswordSecondFormPage(driver)

        start_page.click_on_button_personal_account()
        login_page.click_on_button_recovery_password()

        email, password, name = generate_email_password_name()
        recovery_pas_page.send_email(text=email)
        recovery_pas_page.click_on_button_recovery()

        assert recovery_pas_page_s_f.return_current_url() == 'https://stellarburgers.nomoreparties.site/reset-password'

    @allure.title('клик по кнопке показать/скрыть пароль делает поле активным — подсвечивает его')
    def test_click_on_button_show_and_hide_makes_field_active(self, driver):
        start_page = StartPage(driver)
        login_page = LoginPage(driver)
        recovery_pas_page = RecoveryPasswordPage(driver)
        recovery_pas_page_s_f= RecoveryPasswordSecondFormPage(driver)

        start_page.click_on_button_personal_account()
        login_page.click_on_button_recovery_password()

        email, password, name = generate_email_password_name()
        recovery_pas_page.send_email(text=email)
        recovery_pas_page.click_on_button_recovery()
        recovery_pas_page_s_f.click_on_button_show_and_hide_password()

        assert 'input pr-6 pl-6 input_type_text input_size_default input_status_active' == recovery_pas_page_s_f.get_status_button_input_password()
