import time
import allure
from pages.base_page import BasePage
from locators.feed_order_page_locators import FeedOrderPageLocators

class FeedOrderPage(BasePage):

    @allure.step('Нажатие на карточку последнего заказа')
    def click_on_last_order(self):
        self.click_on_element(locator=FeedOrderPageLocators.last_order)

    @allure.step('возвращение статуса окна с информацией о заказе')
    def return_status_window_with_info_order(self):
        text_info_order = self.find_element(locator=FeedOrderPageLocators.window_with_info_order)
        return text_info_order.get_attribute('class')

    @allure.step('получение номера последнего заказа')
    def get_number_last_order(self):
        self.wait_for_element_to_have_text(locator=FeedOrderPageLocators.number_last_order)
        return self.find_element(locator=FeedOrderPageLocators.number_last_order).text

    @allure.step('получение значения счетчика заказов за все время')
    def get_all_time_completed_counter(self):
        self.wait_for_element_to_have_text(locator=FeedOrderPageLocators.all_time_completed_counter)
        return self.find_element(locator=FeedOrderPageLocators.all_time_completed_counter).text

    @allure.step('получение значения счетчика заказов за сегодня')
    def get_today_completed_counter(self):
        self.wait_for_element_to_have_text(locator=FeedOrderPageLocators.today_completed_counter)
        return self.find_element(locator=FeedOrderPageLocators.today_completed_counter).text

    @allure.step('Получение номера заказа, который находится в работе')
    def get_order_in_work(self):
        self.wait_for_modal_to_close()
        return self.find_element(locator=FeedOrderPageLocators.in_work).text

    @allure.step('Ожидание смены текста счетчика на номер заказа')
    def wait_for_text_fot_counter_all_time_to_change(self):
        self.wait_for_text_to_change(text_none='Все текущие заказы готовы!', locator=FeedOrderPageLocators.in_work)

    @allure.step('Ожидание смены адреса страницы')
    def wait_current_url(self):
        self.wait_url('https://stellarburgers.nomoreparties.site/feed')
