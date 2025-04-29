from selenium.webdriver.common.by import By

class PersonalUserProfilePageLocators:

    button_order_history = [By.XPATH, './/a[@class="Account_link__2ETsJ text text_type_main-medium text_color_inactive"]']
    button_exit = [By.XPATH, './/button[@class="Account_button__14Yp3 text text_type_main-medium text_color_inactive"]']
    last_order = [By.XPATH, './/ul[@class="OrderHistory_profileList__374GU OrderHistory_list__KcLDB"]/li[last()]/a/div/p[@class="text text_type_digits-default"]']