from selenium.webdriver.common.by import By


class RecoveryPasswordSecondFormPageLocators:

    button_input_password = [By.XPATH, './/div[@class="input pr-6 pl-6 input_type_password input_size_default"]']
    button_input_password_after_click = [By.XPATH, './/div[@class="input__icon input__icon-action"]/..']
    button_show_and_hide_password = [By.XPATH, './/div[@class="input__icon input__icon-action"]']


