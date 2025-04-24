import time
import allure
from pages.base_page import BasePage
from locators.feed_order_page_locators import FeedOrderPageLocators

class FeedOrderPage(BasePage):

    @allure.step('Нажатие на карточку последнего заказа')
    def click_on_last_order(self):
        time.sleep(1)
        self.click_on_element(locator=FeedOrderPageLocators.last_order)

    @allure.step('возвращение статуса окна с информацией о заказе')
    def return_status_window_with_info_order(self):
        time.sleep(1)
        text_info_order = self.find_element(locator=FeedOrderPageLocators.window_with_info_order)
        return text_info_order.get_attribute('class')

    @allure.step('получение номера последнего заказа')
    def get_number_last_order(self):
        return self.find_element(locator=FeedOrderPageLocators.number_last_order).text

    @allure.step('получение значения счетчика заказов за все время')
    def get_all_time_completed_counter(self):
        return self.find_element(locator=FeedOrderPageLocators.all_time_completed_counter).text

    @allure.step('получение значения счетчика заказов за сегодня')
    def get_today_completed_counter(self):
        return self.find_element(locator=FeedOrderPageLocators.today_completed_counter).text

    @allure.step('Получение номера заказа, который находится в работе')
    def get_order_in_work(self):
        return self.find_element(locator=FeedOrderPageLocators.in_work).text