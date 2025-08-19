from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.rendering_block_locators import RenderingBlockLocators
from locators.drawing_route_locators import DrawingRouteLocators
from data import Addresses


class RenderingBlockPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)
        self.locators = RenderingBlockLocators()

    def set_same_address(self):
        from_field = self.driver.find_element(*DrawingRouteLocators.FIELD_FROM)
        from_field.clear()
        from_field.send_keys(Addresses.KHAMOVNICHESKY_VAL)

        where_field = self.driver.find_element(*DrawingRouteLocators.FIELD_WHERE)
        where_field.clear()
        where_field.send_keys(Addresses.KHAMOVNICHESKY_VAL)

    def is_route_block_displayed(self):
        """Проверяет, отображается ли блок с маршрутом"""
        try:
            return self.wait.until(
                EC.visibility_of_element_located(self.locators.ROUTE_SELECTION_BLOCK)
            ).is_displayed()
        except:
            return False

    def get_same_address_message(self):
        """Возвращает текст сообщения для одинаковых адресов"""
        element = self.wait.until(
            EC.visibility_of_element_located(self.locators.SAME_ADDRESS_MESSAGE)
        )
        return element.text

    def is_text_present(self, text):
        """Проверяет наличие текста на странице"""
        try:
            locator = (self.locators.ANY_TEXT_ELEMENT[0],
                      self.locators.ANY_TEXT_ELEMENT[1].format(text))
            self.wait.until(EC.presence_of_element_located(locator))
            return True
        except:
            return False