import allure
from page.locators import *
from selenium.webdriver.common.keys import Keys
from selenium import webdriver

class BasePage:
    def __init__(self, driver):
        self.driver = driver

    @allure.step(f"Открытие браузера на странице {MainPageLocators.url}")
    def go_to_site(self):
        self.driver.get(MainPageLocators.url)

    @allure.step("Скролл до вопросов")
    def scroll_to_page_end(self):
        self.driver.execute_script("window.scrollTo(0, document.body.scrollHeight);")

    @allure.step("Скролл до кнопки заказа на середины страницы")
    def scroll_till_middle_page(self):
        self.driver.execute_script("window.scrollBy(0, 1500);")
