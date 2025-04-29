from selenium.webdriver.common.by import By
from helpers.auxiliary_functions_for_api import choice_random_sauce


class StartPageLocators:

    logo_button = [By.XPATH, './/div[@class="AppHeader_header__logo__2D0X2"]']
    button_designer = [By.XPATH, './/p[text()="Конструктор"]']
    button_order_feed = [By.XPATH, './/p[text()="Лента Заказов"]']
    button_personal_account = [By.XPATH, './/p[text()="Личный Кабинет"]']
    button_place_an_order = [By.XPATH, './/button[text()="Оформить заказ"]']
    window_order_creation = [By.XPATH, './/p[text()="Ваш заказ начали готовить"]']

    random_ingredient = [By.XPATH, f'.//img[@alt="{choice_random_sauce()}"]']
    cross_on_window_ingredient = [By.XPATH, './/div[@class="Modal_modal__contentBox__sCy8X pt-10 pb-15"]/following-sibling::button']
    cross_on_window_order = [By.XPATH, './/button[@class="Modal_modal__close_modified__3V5XS Modal_modal__close__TnseK"]']
    window_ingredient = [By.XPATH, './/h2[text()="Детали ингредиента"]/../../..']
    locator_target_for_order = [By.XPATH, './/ul[@class="BurgerConstructor_basket__list__l9dp_"]']
    number_order_in_window_about_order = [By.XPATH, './/h2[@class="Modal_modal__title_shadow__3ikwq Modal_modal__title__2L34m text text_type_digits-large mb-8"]']

    souse_spicy_x = [By.XPATH, './/img[@alt="Соус Spicy-X"]']
    counter_souse_spicy_x = [By.XPATH, './/img[@alt="Соус Spicy-X"]/preceding-sibling::div[@class="counter_counter__ZNLkj counter_default__28sqi"]/p']
    bread_r2 = [By.XPATH, './/img[@alt="Флюоресцентная булка R2-D3"]']

    modal_locator = [By.CLASS_NAME, "Modal_modal__loading__3534A"]