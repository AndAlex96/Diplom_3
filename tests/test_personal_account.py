from conftest import driver, created_user
from pages.login_page import LoginPage
from pages.personal_user_profile_page import PersonalUserProfilePage
from pages.start_page import StartPage
import allure

class TestPersonalAccount:

    @allure.title('переход по клику на «Личный кабинет»')
    def test_transition_by_click_in_personal_account(self, driver):
        start_page = StartPage(driver)
        login_page = LoginPage(driver)

        start_page.click_on_button_personal_account()

        assert login_page.return_current_url() == "https://stellarburgers.nomoreparties.site/login"

    @allure.title('переход в раздел «История заказов»')
    def test_go_to_the_order_history_section(self, driver, created_user):
        email, password, name = created_user

        start_page = StartPage(driver)
        login_page = LoginPage(driver)
        personal_user_prof = PersonalUserProfilePage(driver)

        start_page.click_on_button_personal_account()

        login_page.filling_in_the_email_field(text=email)
        login_page.filling_in_the_password_field(text=password)
        login_page.click_on_login_button()
        start_page.click_on_button_personal_account()
        personal_user_prof.click_on_button_orders_history()

        assert personal_user_prof.get_current_url_on_user_page() == 'https://stellarburgers.nomoreparties.site/account/order-history'

    @allure.title('выход из аккаунта')
    def test_exit_of_account(self, driver, created_user):
        email, password, name = created_user

        start_page = StartPage(driver)
        login_page = LoginPage(driver)
        personal_user_prof = PersonalUserProfilePage(driver)

        start_page.click_on_button_personal_account()

        login_page.filling_in_the_email_field(text=email)
        login_page.filling_in_the_password_field(text=password)
        login_page.click_on_login_button()
        start_page.click_on_button_personal_account()
        personal_user_prof.click_on_button_exit()

        assert login_page.return_current_url() == 'https://stellarburgers.nomoreparties.site/login'
