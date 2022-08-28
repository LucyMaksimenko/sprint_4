from selenium.webdriver.common.by import By

class MainPageLocators:
    url = "https://qa-scooter.praktikum-services.ru/"
    question_price = (By.ID, "accordion__heading-0")
    answer_price = (By.ID, "accordion__panel-0")
    question_few_scooters = (By.ID, "accordion__heading-1")
    answer_few_scooters = (By.ID, "accordion__panel-1")
    question_rent_time = (By.ID, "accordion__heading-2")
    answer_rent_time = (By.ID, "accordion__panel-2")
    question_take_scooter_today = (By.ID, "accordion__heading-3")
    answer_take_scooter_today = (By.ID, "accordion__panel-3")
    question_prolong_scooter = (By.ID, "accordion__heading-4")
    answer_prolong_scooter = (By.ID, "accordion__panel-4")
    question_charge_with_scooter = (By.ID, "accordion__heading-5")
    answer_charge_with_scooter = (By.ID, "accordion__panel-5")
    question_cancel_order = (By.ID, "accordion__heading-6")
    answer_cancel_order = (By.ID, "accordion__panel-6")
    question_beyond_mkad = (By.ID, "accordion__heading-7")
    answer_beyond_mkad = (By.ID, "accordion__panel-7")


class OrderFlowLocators:
    order_button_top = (By.CLASS_NAME, "Button_Button__ra12g")
    order_button_middle = (By.CSS_SELECTOR, "[class='Button_Button__ra12g Button_Middle__1CSJM']")
    scooter_logo = (By.CLASS_NAME, "Header_LogoScooter__3lsAR")
    yandex_logo = (By.CLASS_NAME, "Header_LogoYandex__3TSOI")
    name_input = (By.CSS_SELECTOR, "[placeholder='* Имя']")
    last_name_input = (By.CSS_SELECTOR, "[placeholder='* Фамилия']")
    address_input = (By.CSS_SELECTOR, "[placeholder='* Адрес: куда привезти заказ']")
    metro_station_dropdown = (By.CSS_SELECTOR, "[placeholder='* Станция метро']")
    phone_input = (By.CSS_SELECTOR, "[placeholder='* Телефон: на него позвонит курьер']")
    next_button = (By.CSS_SELECTOR, "[class='Button_Button__ra12g Button_Middle__1CSJM']")
    date_for_delivery = (By.CSS_SELECTOR, "[placeholder='* Когда привезти самокат']")
    rent_period = (By.CLASS_NAME, "Dropdown-control")
    one_day_period = (By.XPATH, ".//div[contains(text(),'сутки')]")
    four_day_period = (By.XPATH, ".//div[contains(text(),'четверо суток')]")
    black_color_checkbox = (By.CSS_SELECTOR, "[id='black']")
    grey_color_checkbox = (By.CSS_SELECTOR, "[id='grey']")
    comment_for_courier = (By.CSS_SELECTOR, "[placeholder='Комментарий для курьера']")
    yes_button = (By.XPATH, ".//button[contains(text(),'Да')]")
    success_order_confirmation = (By.XPATH, ".//div[contains(text(), 'Заказ оформлен')]")





