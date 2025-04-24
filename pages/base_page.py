from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.action_chains import ActionChains
from conftest import driver
import pytest
import allure


class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step('Поиск элемента')
    @pytest.mark.usefixtures("driver")
    def find_element(self, locator):
        WebDriverWait(self.driver, 10).until(EC.visibility_of_element_located(locator))
        return WebDriverWait(self.driver, 10).until(EC.element_to_be_clickable(locator))

    @allure.step('Нажатие на элемент')
    @pytest.mark.usefixtures("driver")
    def click_on_element(self, locator):
        self.driver.find_element(*locator).click()

    @allure.step('Получение текущего url')
    @pytest.mark.usefixtures("driver")
    def get_current_url(self):
        WebDriverWait(self.driver, 10)
        return self.driver.current_url

    @allure.step('Ввод текста')
    def input_text(self, locator, text):
        self.find_element(locator).send_keys(text)

    @allure.step('Перемещение элемента')
    @pytest.mark.usefixtures("driver")
    def move_element(self, locator_source, locator_target):
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