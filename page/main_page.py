from page.base_page import *
from selenium.webdriver.support import expected_conditions as ec
from selenium.webdriver.support.wait import WebDriverWait


class MainPage(BasePage):

    def price_question(self):
        self.scroll_to_page_end()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.question_price))
        self.driver.find_element(*MainPageLocators.question_price).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.answer_price))

    def question_few_scooters(self):
        self.scroll_to_page_end()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.question_few_scooters))
        self.driver.find_element(*MainPageLocators.question_few_scooters).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.answer_few_scooters))

    def question_rent_time(self):
        self.scroll_to_page_end()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.question_rent_time))
        self.driver.find_element(*MainPageLocators.question_rent_time).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.answer_rent_time))

    def question_take_scooter_today(self):
        self.scroll_to_page_end()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.question_take_scooter_today))
        self.driver.find_element(*MainPageLocators.question_take_scooter_today).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.answer_take_scooter_today))

    def question_prolong_scooter(self):
        self.scroll_to_page_end()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.question_prolong_scooter))
        self.driver.find_element(*MainPageLocators.question_prolong_scooter).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.answer_prolong_scooter))

    def question_charge_with_scooter(self):
        self.scroll_to_page_end()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.question_charge_with_scooter))
        self.driver.find_element(*MainPageLocators.question_charge_with_scooter).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.answer_charge_with_scooter))

    def question_cancel_order(self):
        self.scroll_to_page_end()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.question_cancel_order))
        self.driver.find_element(*MainPageLocators.question_cancel_order).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.answer_cancel_order))

    def question_beyond_mkad(self):
        self.scroll_to_page_end()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.question_beyond_mkad))
        self.driver.find_element(*MainPageLocators.question_beyond_mkad).click()
        WebDriverWait(self.driver, 5).until(ec.visibility_of_element_located(MainPageLocators.answer_beyond_mkad))

    def go_to_scooter_page_from_logo(self):
        self.driver.find_element(*OrderFlowLocators.order_button_top).click()
        self.driver.find_element(*OrderFlowLocators.scooter_logo).click()

    def go_to_yandex_page(self):
        self.driver.find_element(*OrderFlowLocators.yandex_logo).click()
        self.driver.switch_to.window(self.driver.window_handles[1])
        WebDriverWait(self.driver, 5).until(ec.url_contains("https://yandex.ru/"))


