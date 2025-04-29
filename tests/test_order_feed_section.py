from conftest import driver
from pages.feed_order_page import FeedOrderPage
from pages.start_page import StartPage
from pages.login_page import LoginPage
from pages.personal_user_profile_page import PersonalUserProfilePage
import allure


class TestOrderFeedSection:

    @allure.title('если кликнуть на заказ, откроется всплывающее окно с деталями')
    def test_open_window_with_info_order(self, driver):
        start_page = StartPage(driver)
        feed_order_page = FeedOrderPage(driver)

        start_page.click_on_button_orders_feed()
        feed_order_page.click_on_last_order()

        assert feed_order_page.return_status_window_with_info_order() == 'text text_type_digits-default mb-10 mt-5'

    @allure.title('заказы пользователя из раздела «История заказов» отображаются на странице «Лента заказов»')
    def test_order_reflection_from_the_order_history_in_the_order_feed(self, driver, created_user):
        email, password, name = created_user

        start_page = StartPage(driver)
        login_page = LoginPage(driver)
        personal_user_prof = PersonalUserProfilePage(driver)
        feed_order_page = FeedOrderPage(driver)

        start_page.click_on_button_personal_account()
        login_page.filling_in_the_email_field(text=email)
        login_page.filling_in_the_password_field(text=password)
        login_page.click_on_login_button()

        start_page.get_ingredient_in_order()
        start_page.get_bread_in_order()
        start_page.click_on_button_place_an_order()
        start_page.click_on_cross_button_on_window_order()

        start_page.click_on_button_personal_account()
        personal_user_prof.wait_current_url()
        personal_user_prof.click_on_button_orders_history()
        number_order = personal_user_prof.get_number_last_order()
        start_page.click_on_button_orders_feed()

        assert number_order == feed_order_page.get_number_last_order()

    @allure.title('при создании нового заказа счётчик Выполнено за всё время увеличивается')
    def test_when_creating_a_new_order_the_completed_for_all_time_counter_increases(self, driver, created_user):
        email, password, name = created_user

        start_page = StartPage(driver)
        login_page = LoginPage(driver)
        feed_order_page = FeedOrderPage(driver)

        start_page.click_on_button_personal_account()
        login_page.filling_in_the_email_field(text=email)
        login_page.filling_in_the_password_field(text=password)
        login_page.click_on_login_button()

        start_page.wait_loading_url()
        start_page.click_on_button_orders_feed()
        feed_order_page.wait_current_url()
        before_number = feed_order_page.get_all_time_completed_counter()

        start_page.click_on_logo_button()

        start_page.get_ingredient_in_order()
        start_page.get_bread_in_order()
        start_page.click_on_button_place_an_order()
        start_page.click_on_cross_button_on_window_order()

        start_page.click_on_button_orders_feed()
        feed_order_page.wait_current_url()
        feed_order_page.wait_for_text_fot_counter_all_time_to_change()

        assert before_number != feed_order_page.get_all_time_completed_counter()

    @allure.title('при создании нового заказа счётчик Выполнено за сегодня увеличивается')
    def test_when_create_a_new_order_the_completed_for_today_counter_increases(self, driver, created_user):
        email, password, name = created_user

        start_page = StartPage(driver)
        login_page = LoginPage(driver)
        feed_order_page = FeedOrderPage(driver)

        start_page.click_on_button_personal_account()
        login_page.filling_in_the_email_field(text=email)
        login_page.filling_in_the_password_field(text=password)
        login_page.click_on_login_button()

        start_page.wait_loading_url()
        start_page.click_on_button_orders_feed()
        feed_order_page.wait_current_url()
        before_number = feed_order_page.get_today_completed_counter()

        start_page.click_on_logo_button()
        start_page.wait_loading_url()

        start_page.get_ingredient_in_order()
        start_page.get_bread_in_order()
        start_page.click_on_button_place_an_order()
        start_page.wait_for_modal_to_close()
        start_page.click_on_cross_button_on_window_order()

        start_page.click_on_button_orders_feed()
        feed_order_page.wait_current_url()
        feed_order_page.wait_for_text_fot_counter_all_time_to_change()

        assert before_number != feed_order_page.get_today_completed_counter()

    @allure.title('после оформления заказа его номер появляется в разделе В работе')
    def test_after_placing_an_order_its_number_appears_in_the_in_progress_section(self, driver, created_user):
        email, password, name = created_user

        start_page = StartPage(driver)
        login_page = LoginPage(driver)
        feed_order_page = FeedOrderPage(driver)

        start_page.click_on_button_personal_account()
        login_page.filling_in_the_email_field(text=email)
        login_page.filling_in_the_password_field(text=password)
        login_page.click_on_login_button()

        start_page.get_ingredient_in_order()
        start_page.get_bread_in_order()
        start_page.click_on_button_place_an_order()
        start_page.wait_for_modal_to_close()
        number_order = start_page.get_number_order_in_window_about_order()
        start_page.click_on_cross_button_on_window_order()

        start_page.click_on_button_orders_feed()
        feed_order_page.wait_for_text_fot_counter_all_time_to_change()
        number_order_in_work = feed_order_page.get_order_in_work()

        assert f'0{number_order}' == number_order_in_work