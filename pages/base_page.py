from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from conftest import driver
import pytest
import allure

from locators.start_page_locators import StartPageLocators


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента')
    @pytest.mark.usefixtures("driver")
    def find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.presence_of_element_located(locator))
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step('Ожидание появления текста у элемента')
    @pytest.mark.usefixtures("driver")
    def wait_for_element_to_have_text(self, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(
            lambda driver: driver.find_element(*locator).text != ""
        )

    @allure.step('Нажатие на элемент')
    @pytest.mark.usefixtures("driver")
    def click_on_element(self, locator):
        action = ActionChains(self.driver)
        WebDriverWait(self.driver, 5).until(EC.element_to_be_clickable(locator))
        element = self.driver.find_element(*locator)
        action.click(on_element=element).perform()

    @allure.step('Получение текущего url')
    @pytest.mark.usefixtures("driver")
    def get_current_url(self, web=None):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(web))
        return self.driver.current_url

    @allure.step('Ожидание загрузки url')
    @pytest.mark.usefixtures("driver")
    def wait_url(self, web):
        WebDriverWait(self.driver, 10).until(EC.url_to_be(web))

    @allure.step('Ожидание закрытия модального окна')
    @pytest.mark.usefixtures("driver")
    def wait_for_modal_to_close(self, modal_locator=StartPageLocators.modal_locator, timeout=10):
        WebDriverWait(self.driver, timeout).until(
                EC.invisibility_of_element_located(modal_locator)
            )

    @allure.step('Ожидание смены текста')
    @pytest.mark.usefixtures("driver")
    def wait_for_text_to_change(self, text_none, locator, timeout=15):
        WebDriverWait(self.driver, timeout).until(
                lambda d: d.find_element(*locator).text != text_none
            )

    @allure.step('Ввод текста')
    @pytest.mark.usefixtures("driver")
    def input_text(self, locator, text):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))
        self.find_element(locator).send_keys(text)

    @allure.step('Перемещение элемента')
    @pytest.mark.usefixtures("driver")
    def move_element(self, locator_source, locator_target):
        WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator_source))
        source = self.driver.find_element(*locator_source)
        target = self.driver.find_element(*locator_target)
        action = ActionChains(self.driver)
        action.drag_and_drop(source, target).pause(5).perform()

    @allure.step('Пролистывание к элементу')
    @pytest.mark.usefixtures("driver")
    def scroll_to_element(self, locator):
        WebDriverWait(self.driver, 5).until(EC.visibility_of_element_located(locator))
        element = self.driver.find_element(*locator)
        self.driver.execute_script("arguments[0].scrollIntoView();", element)