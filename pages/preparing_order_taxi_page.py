from selenium.webdriver.support import expected_conditions as EC
from locators.preparing_order_taxi_locators import PreparingOrderTaxiLocators
from pages.base_page import BasePage


class PreparingOrderTaxiPage(BasePage):
    def switch_to_optimal_mode(self):
        """Кликает на кнопку оптимального режима"""
        self.click_element(PreparingOrderTaxiLocators.OPTIMAL_MODE)
        return self

    def is_optimal_mode_active(self):
        """Проверяет активное состояние оптимального режима"""
        element = self.wait.until(
            EC.visibility_of_element_located(PreparingOrderTaxiLocators.MODE_ACTIVE)
        )
        return "Оптимальный" in element.text

    def is_price_visible(self):
        """Проверяет видимость блока с ценой"""
        return self.wait.until(
            EC.visibility_of_element_located(PreparingOrderTaxiLocators.TEXT_CAR_PRICE)
        ).is_displayed()

    def switch_to_custom_mode(self):
        """Кликает на кнопку своего режима"""
        self.click_element(PreparingOrderTaxiLocators.CUSTOM_MODE)
        return self

    def is_custom_mode_active(self):
        """Проверяет активное состояние своего режима"""
        element = self.wait.until(
            EC.visibility_of_element_located(PreparingOrderTaxiLocators.MODE_ACTIVE)
        )
        return "Свой" in element.text

    def is_call_taxi_button_visible(self):
        """Проверяет видимость кнопки 'Вызвать такси'"""
        return self.wait.until(
            EC.visibility_of_element_located(PreparingOrderTaxiLocators.BUTTON_CALL_TAXI)
        ).is_displayed()

    def is_mode_active(self, mode_name):
        """Проверяет активность любого режима по названию"""
        element = self.wait.until(
            EC.visibility_of_element_located(PreparingOrderTaxiLocators.MODE_ACTIVE)
        )
        return mode_name in element.text

    def select_drive_type(self):
        """Выбирает тип передвижения 'Драйв'"""
        self.click_element(PreparingOrderTaxiLocators.DRIVE_TYPE)
        return self

    def is_book_button_visible(self):
        """Проверяет видимость кнопки 'Забронировать'"""
        return self.wait.until(
            EC.visibility_of_element_located(PreparingOrderTaxiLocators.BUTTON_BOOK)
        ).is_displayed()