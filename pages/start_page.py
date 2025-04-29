import time
import allure
from locators.start_page_locators import StartPageLocators
from pages.base_page import BasePage


class StartPage(BasePage):

    @allure.step('клик по кнопке личный кабинет')
    def click_on_button_personal_account(self):
        self.click_on_element(locator= StartPageLocators.button_personal_account)

    @allure.step('клик по кнопке конструктор')
    def click_on_button_designer(self):
        self.click_on_element(locator=StartPageLocators.button_designer)

    @allure.step('клик по кнопке лента заказов')
    def click_on_button_orders_feed(self):
        self.click_on_element(locator=StartPageLocators.button_order_feed)

    @allure.step('клик на случайный ингридиент')
    def click_on_random_ingredient(self):
        self.click_on_element(locator=StartPageLocators.random_ingredient)

    @allure.step('проверка открытия окна с информацией об ингредиенте')
    def check_open_window_ingredient(self):
        return self.find_element(locator=StartPageLocators.window_ingredient)

    @allure.step('получение атрибута -класса- окна ингридиента')
    def get_class_window_ingredient(self):
        return self.check_open_window_ingredient().get_attribute('class')

    @allure.step('нажатие на кнопку -крестик- закрытия окна ингридиента')
    def click_on_cross_button_on_window_ingredient(self):
        self.click_on_element(locator=StartPageLocators.cross_on_window_ingredient)

    @allure.step('закрытие окна заказа')
    def click_on_cross_button_on_window_order(self):
        self.wait_for_modal_to_close(modal_locator=StartPageLocators.modal_locator)
        self.click_on_element(locator=StartPageLocators.cross_on_window_order)

    @allure.step('получение текущего url')
    def get_current_url_for_designer(self):
        return self.get_current_url('https://stellarburgers.nomoreparties.site/')

    @allure.step('ожидание загрузки страницы')
    def wait_loading_url(self):
        return self.wait_url('https://stellarburgers.nomoreparties.site/')

    @allure.step('получение текущего url')
    def get_current_url_for_feed_order(self):
        return self.get_current_url('https://stellarburgers.nomoreparties.site/feed')

    @allure.step('добавление случайного ингридиента в заказ')
    def get_ingredient_in_order(self):
        self.move_element(locator_source=StartPageLocators.random_ingredient, locator_target=StartPageLocators.locator_target_for_order)

    @allure.step('добавление булки в заказ в заказ')
    def get_bread_in_order(self):
        self.move_element(locator_source=StartPageLocators.bread_r2,
                          locator_target=StartPageLocators.locator_target_for_order)

    @allure.step('добавление соуса спайси икс в заказ')
    def get_souse_spicy_x_in_order(self):
        self.move_element(locator_source=StartPageLocators.souse_spicy_x, locator_target=StartPageLocators.locator_target_for_order)

    @allure.step('получение значения счетчика количества добавленных ингридиентов')
    def get_value_ingredient_counter_souse_spicy_x(self):
        self.scroll_to_element(locator=StartPageLocators.souse_spicy_x)
        value = self.find_element(locator=StartPageLocators.counter_souse_spicy_x).text
        return int(value)

    @allure.step('клик по кнопке оформления заказа')
    def click_on_button_place_an_order(self):
        self.click_on_element(locator=StartPageLocators.button_place_an_order)

    @allure.step('проверка наличия надписи оформления заказа')
    def checking_the_order_creation(self):
        return self.find_element(locator=StartPageLocators.window_order_creation).text

    @allure.step('нажатие на главный логотип сайта')
    def click_on_logo_button(self):
        self.click_on_element(locator=StartPageLocators.logo_button)

    @allure.step('получение номера заказа в окне заказа')
    def get_number_order_in_window_about_order(self):
        self.wait_for_modal_to_close()
        return self.find_element(locator=StartPageLocators.number_order_in_window_about_order).text