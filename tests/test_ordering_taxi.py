import pytest
import allure
from pages.ordering_taxi_page import OrderingTaxiPage
from locators.ordering_taxi_locators import OrderingTaxiLocators


class TestOrderingTaxi:

    @allure.title("Проверка отображения тарифов")
    @allure.description("Тест проверяет, что отображается 6 тарифов и только 1 активный")
    def test_tariffs_displayed_correctly(self, taxi_order_created):
        with allure.step("Проверка количества тарифов"):
            page = OrderingTaxiPage(taxi_order_created)
            assert page.all_tariffs_count == 6
            assert page.active_tariffs_count == 1

    @allure.title("Проверка подсказок тарифов: {tariff_name}")
    @allure.description("Тест проверяет всплывающие подсказки для каждого тарифа")
    def test_tariff_tooltips(self, taxi_order_created, tariff_name):
        if tariff_name in ["Сонный", "Разговорчивый"]:
            pytest.xfail(f"Баг в описании тарифа '{tariff_name}'")
        with allure.step(f"Проверка подсказки для тарифа '{tariff_name}'"):
            page = OrderingTaxiPage(taxi_order_created)
            assert page.check_tariff_tooltip(tariff_name)

    @allure.title("Проверка полей формы заказа")
    @allure.description("Тест проверяет отображение всех обязательных полей формы заказа")
    def test_order_form_fields(self, taxi_order_created):
        page = OrderingTaxiPage(taxi_order_created)
        with allure.step("Проверка поля 'Телефон'"):
            assert page.is_phone_field_visible(), "Поле 'Телефон' не отображается"
        with allure.step("Проверка поля 'Способ оплаты'"):
            assert page.is_payment_method_visible(), "Поле 'Способ оплаты' не отображается"
        with allure.step("Проверка поля 'Комментарий водителю'"):
            assert page.is_driver_comment_visible(), "Поле 'Комментарий водителю' не отображается"
        with allure.step("Проверка поля 'Требования к заказу'"):
            assert page.is_requirements_visible(), "Поле 'Требование к заказу' не отображается"

    @allure.title("Полный процесс заказа такси")
    @allure.description("Тест проверяет полный workflow заказа такси от выбора до подтверждения")
    def test_complete_taxi_order_workflow(self, taxi_order_created):
        page = OrderingTaxiPage(taxi_order_created)
        with allure.step("Клик на 'Требования к заказу'"):
            page.scroll_and_click_requirements()
        with allure.step("Активация 'Столик для ноутбука'"):
            page.click_element(OrderingTaxiLocators.TOGGLE_SWITCH)
        with allure.step("Подтверждение заказа"):
            page.click_element(OrderingTaxiLocators.SUBMIT_BUTTON)
        with allure.step("Проверка окна ожидания"):
            assert page.is_element_visible(OrderingTaxiLocators.CLOSE_BUTTON)

    @allure.title("Ожидание завершения заказа и проверка номера")
    @allure.description("Тест проверяет появление номера заказа после завершения таймера")
    def test_wait_for_timer_and_check_order(self, taxi_order_created):
        page = OrderingTaxiPage(taxi_order_created)
        with allure.step("Выполнение шагов заказа"):
            page.scroll_and_click_requirements()
            page.click_element(OrderingTaxiLocators.TOGGLE_SWITCH)
            page.click_element(OrderingTaxiLocators.SUBMIT_BUTTON)
        with allure.step("Ожидание номера заказа (45 секунд)"):
            assert page.is_element_visible(OrderingTaxiLocators.ORDER_NUMBER, timeout=45), \
                "Номер заказа не появился на экране в течение 45 секунд"

    @allure.title("Проверка сохранения стоимости заказа")
    @allure.description("Тест проверяет, что стоимость не меняется в процессе оформления")
    def test_price_consistency_numeric(self, taxi_order_created):
        page = OrderingTaxiPage(taxi_order_created)
        with allure.step("Получение первоначальной стоимости"):
            initial_price_text = page.get_text(OrderingTaxiLocators.TAXI_PRICE)
            initial_price_value = page.extract_price_value(initial_price_text)
        with allure.step("Оформление заказа"):
            page.scroll_and_click_requirements()
            page.click_element(OrderingTaxiLocators.TOGGLE_SWITCH)
            page.click_element(OrderingTaxiLocators.SUBMIT_BUTTON)
        with allure.step("Открытие меню"):
            page.click_element(OrderingTaxiLocators.BURGER_MENU_BUTTON)
        with allure.step("Проверка стоимости в деталях заказа"):
            order_price_text = page.get_text(OrderingTaxiLocators.ORDER_PRICE)
            order_price_value = page.extract_price_value(order_price_text)
        with allure.step("Сравнение стоимостей"):
            assert initial_price_value == order_price_value

    @allure.title("Проверка отмены заказа")
    @allure.description("Тест проверяет закрытие окна заказа при нажатии на крестик")
    @pytest.mark.xfail(reason="Баг: при клике на крестик окно не закрывается")
    def test_cancel_order_and_close_window(self, taxi_order_created):
        page = OrderingTaxiPage(taxi_order_created)
        with allure.step("Создание заказа"):
            page.scroll_and_click_requirements()
            page.click_element(OrderingTaxiLocators.TOGGLE_SWITCH)
            page.click_element(OrderingTaxiLocators.SUBMIT_BUTTON)
        with allure.step("Клик на кнопку закрытия"):
            page.click_element(OrderingTaxiLocators.CLOSE_BUTTON)
        with allure.step("Проверка закрытия окна"):
            assert not page.is_element_visible(OrderingTaxiLocators.CLOSE_BUTTON, timeout=5), \
                "Окно не закрылось после нажатия кнопки Отмена"
