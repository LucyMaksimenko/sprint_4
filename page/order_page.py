from selenium.webdriver import Keys
from page.base_page import *
import datetime
from datetime import timedelta

tomorrow_date = str(datetime.date.today() + timedelta(days=1))

class OrderPage(BasePage):
    def go_to_order_page_from_top_button(self):
        self.driver.find_element(*OrderFlowLocators.order_button_top).click()

    def go_to_order_page_from_middle_button(self):
        self.scroll_till_middle_page()
        self.driver.find_element(*OrderFlowLocators.order_button_middle).click()

    def customer_info_filling(self):
        self.driver.find_element(*OrderFlowLocators.name_input).send_keys("Тест")
        self.driver.find_element(*OrderFlowLocators.last_name_input).send_keys("Тестович")
        self.driver.find_element(*OrderFlowLocators.address_input).send_keys("деревня Комарово")
        self.driver.find_element(*OrderFlowLocators.metro_station_dropdown).click()
        self.driver.find_element(*OrderFlowLocators.metro_station_dropdown).send_keys(Keys.ARROW_DOWN + Keys.ENTER)
        self.driver.find_element(*OrderFlowLocators.phone_input).send_keys("89111111111")
        self.driver.find_element(*OrderFlowLocators.next_button).click()

    def rent_black_for_one_day_filling_info(self):
        self.driver.find_element(*OrderFlowLocators.date_for_delivery).click()
        self.driver.find_element(*OrderFlowLocators.date_for_delivery).send_keys(tomorrow_date + Keys.ENTER)
        self.driver.find_element(*OrderFlowLocators.rent_period).click()
        self.driver.find_element(*OrderFlowLocators.one_day_period).click()
        self.driver.find_element(*OrderFlowLocators.black_color_checkbox).click()
        self.driver.find_element(*OrderFlowLocators.comment_for_courier).send_keys("тестовый заказ")
        self.driver.find_element(*OrderFlowLocators.order_button_middle).click()
        self.driver.find_element(*OrderFlowLocators.yes_button).click()

    def rent_grey_for_four_day_filling_info(self):
        self.driver.find_element(*OrderFlowLocators.date_for_delivery).click()
        self.driver.find_element(*OrderFlowLocators.date_for_delivery).send_keys(tomorrow_date + Keys.ENTER)
        self.driver.find_element(*OrderFlowLocators.rent_period).click()
        self.driver.find_element(*OrderFlowLocators.four_day_period).click()
        self.driver.find_element(*OrderFlowLocators.grey_color_checkbox).click()
        self.driver.find_element(*OrderFlowLocators.comment_for_courier).send_keys("тестовый заказ")
        self.driver.find_element(*OrderFlowLocators.order_button_middle).click()
        self.driver.find_element(*OrderFlowLocators.yes_button).click()
