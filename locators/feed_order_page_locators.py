from selenium.webdriver.common.by import By

class FeedOrderPageLocators:

    last_order = [By.XPATH, './/ul[@class="OrderFeed_list__OLh59"]/li']
    number_last_order = [By.XPATH, './/ul[@class="OrderFeed_list__OLh59"]/li/a/div/p[@class="text text_type_digits-default"]']
    window_with_info_order = [By.XPATH, './/p[@class="text text_type_digits-default mb-10 mt-5"]']
    in_work = [By.XPATH, './/div[@class="OrderFeed_orderStatusBox__1d4q2 mb-15"]/ul[@class="OrderFeed_orderListReady__1YFem OrderFeed_orderList__cBvyi"]/li']
    today_completed_counter = [By.XPATH, './/p[text()="Выполнено за сегодня:"]/following-sibling::p']
    all_time_completed_counter = [By.XPATH, './/div[@class="OrderFeed_orderStatusBox__1d4q2 mb-15"]/following-sibling::div[@class="undefined mb-15"]/p[@class="OrderFeed_number__2MbrQ text text_type_digits-large"]']