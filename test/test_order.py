from page.order_page import *
from page.locators import *
import allure

class TestOrdersFlow:
    @allure.title("Заказ черного самоката на один день через верхнюю кнопку Заказа")
    def test_order_black_for_one_day_from_top_button(self, driver):
        order = OrderPage(driver)
        order.go_to_site()
        order.go_to_order_page_from_top_button()
        order.customer_info_filling()
        order.rent_black_for_one_day_filling_info()
        assert driver.find_element(*OrderFlowLocators.success_order_confirmation)


    @allure.title("Заказ серого самоката на четыре дня через кнопку Заказа на середине страницы")
    def test_order_grey_for_four_day_from_middle_button(self, driver):
        order = OrderPage(driver)
        order.go_to_site()
        order.go_to_order_page_from_middle_button()
        order.customer_info_filling()
        order.rent_grey_for_four_day_filling_info()
        assert driver.find_element(*OrderFlowLocators.success_order_confirmation)


