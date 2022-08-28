from page.main_page import *
from page.locators import *
import allure

class TestQuestionsBlock:
    @allure.title("Вопрос про стоимость")
    def test_question_price(self, driver):
        page = MainPage(driver)
        page.go_to_site()
        page.price_question()
        assert "Сутки — 400 рублей. Оплата курьеру — наличными или картой." in driver.find_element(*MainPageLocators.answer_price).text

    @allure.title("Вопрос про аренду нескольких самокатов")
    def test_question_few_scooters(self, driver):
        page = MainPage(driver)
        page.go_to_site()
        page.question_few_scooters()
        assert "Пока что у нас так: один заказ — один самокат. Если хотите покататься с друзьями, можете просто сделать несколько заказов — один за другим." in driver.find_element(*MainPageLocators.answer_few_scooters).text

    @allure.title("Вопрос про рассчет времени аренды")
    def test_question_rent_time(self, driver):
        page = MainPage(driver)
        page.go_to_site()
        page.question_rent_time()
        assert "Допустим, вы оформляете заказ на 8 мая. Мы привозим самокат 8 мая в течение дня. Отсчёт времени аренды начинается с момента, когда вы оплатите заказ курьеру. Если мы привезли самокат 8 мая в 20:30, суточная аренда закончится 9 мая в 20:30." in driver.find_element(*MainPageLocators.answer_rent_time).text

    @allure.title("Вопрос про аренду на сегодня")
    def test_question_take_scooter_today(self, driver):
        page = MainPage(driver)
        page.go_to_site()
        page.question_take_scooter_today()
        assert "Только начиная с завтрашнего дня. Но скоро станем расторопнее." in driver.find_element(*MainPageLocators.answer_take_scooter_today).text

    @allure.title("Вопрос про продление аренды")
    def test_question_prolong_scooter(self, driver):
        page = MainPage(driver)
        page.go_to_site()
        page.question_prolong_scooter()
        assert "Пока что нет! Но если что-то срочное — всегда можно позвонить в поддержку по красивому номеру 1010." in driver.find_element(*MainPageLocators.answer_prolong_scooter).text

    @allure.title("Вопрос про зарядку для самоката")
    def test_question_charge_with_scooter(self, driver):
        page = MainPage(driver)
        page.go_to_site()
        page.question_charge_with_scooter()
        assert "Самокат приезжает к вам с полной зарядкой. Этого хватает на восемь суток — даже если будете кататься без передышек и во сне. Зарядка не понадобится." in driver.find_element(*MainPageLocators.answer_charge_with_scooter).text

    @allure.title("Вопрос про отмену аренды")
    def test_question_cancel_order(self, driver):
        page = MainPage(driver)
        page.go_to_site()
        page.question_cancel_order()
        assert "Да, пока самокат не привезли. Штрафа не будет, объяснительной записки тоже не попросим. Все же свои." in driver.find_element(*MainPageLocators.answer_cancel_order).text

    @allure.title("Вопрос про доставку за МКАД")
    def test_question_beyond_mkad(self, driver):
        page = MainPage(driver)
        page.go_to_site()
        page.question_beyond_mkad()
        assert "Да, обязательно. Всем самокатов! И Москве, и Московской области." in driver.find_element(*MainPageLocators.answer_beyond_mkad).text

class TestRedirectingButtons:
    @allure.title("Переход на главную страницу Яндекса по клику на лого")
    @allure.description("Проверка перехода на https://yandex.ru/")
    def test_go_to_yandex_page_from_logo(self, driver):
        yandex_page = MainPage(driver)
        yandex_page.go_to_site()
        yandex_page.go_to_yandex_page()
        assert driver.current_url == "https://yandex.ru/"

    @allure.title("Переход на главную страницу Самоката по кнопке лого со страницы Заказа")
    def test_go_to_scooter_page_from_logo(self, driver):
        scooter_page = MainPage(driver)
        scooter_page.go_to_site()
        scooter_page.go_to_scooter_page_from_logo()
        assert driver.current_url == MainPageLocators.url

