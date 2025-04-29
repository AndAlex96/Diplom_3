from conftest import driver
import allure
from pages.login_page import LoginPage
from pages.start_page import StartPage


class TestCheckingBasicFunctionality:

    @allure.title('переход по клику на «Конструктор»')
    def test_click_through_to_the_constructor(self, driver):
        start_page = StartPage(driver)

        start_page.click_on_button_personal_account()
        start_page.click_on_button_designer()

        assert start_page.get_current_url_for_designer() == 'https://stellarburgers.nomoreparties.site/'

    @allure.title('переход по клику на «Лента заказов»')
    def test_click_through_to_the_order_feed(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_button_orders_feed()

        assert start_page.get_current_url_for_feed_order() == 'https://stellarburgers.nomoreparties.site/feed'

    @allure.title('если кликнуть на ингредиент, появится всплывающее окно с деталями')
    def test_after_clicking_on_an_ingredient_a_popup_window_with_details(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_random_ingredient()

        assert start_page.get_class_window_ingredient() == 'Modal_modal_opened__3ISw4 Modal_modal__P3_V5'

    @allure.title('всплывающее окно закрывается кликом по крестику')
    def test_the_popup_window_closed_by_clicking_on_the_cross(self, driver):
        start_page = StartPage(driver)
        start_page.click_on_random_ingredient()
        start_page.click_on_cross_button_on_window_ingredient()

        assert start_page.get_class_window_ingredient() == 'Modal_modal__P3_V5'

    @allure.title('при добавлении ингредиента в заказ, увеличивается каунтер данного ингредиента')
    def test_ingredient_added_to_the_order_the_counter_of_this_ingredient_increases(self, driver):
        start_page = StartPage(driver)

        start_page.get_souse_spicy_x_in_order()

        assert start_page.get_value_ingredient_counter_souse_spicy_x() == 1

    @allure.title('залогиненный пользователь может оформить заказ')
    def test_a_logged_in_user_can_place_an_order(self, driver, created_user):
        email, password, name = created_user

        start_page = StartPage(driver)
        login_page = LoginPage(driver)

        start_page.click_on_button_personal_account()

        login_page.filling_in_the_email_field(text=email)
        login_page.filling_in_the_password_field(text=password)
        login_page.click_on_login_button()

        start_page.get_ingredient_in_order()
        start_page.click_on_button_place_an_order()

        assert start_page.checking_the_order_creation() == 'Ваш заказ начали готовить'



