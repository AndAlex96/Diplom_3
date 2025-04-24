from selenium.webdriver.common.by import By

class LoginPageLocators:

    input_email = [By.XPATH, './/label[text()="Email"]/following-sibling::input']
    input_password = [By.XPATH, './/label[text()="Пароль"]/following-sibling::input']
    button_login = [By.XPATH, './/button[text()="Войти"]']
    button_password_recovery = [By.XPATH, './/a[text()="Восстановить пароль"]']