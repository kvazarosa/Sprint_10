from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from locators.ordering_taxi_locators import OrderingTaxiLocators
from locators.drawing_route_locators import DrawingRouteLocators
from pages.base_page import BasePage
from selenium.webdriver.support import expected_conditions as EC


class OrderingTaxiPage(BasePage):
    @property
    def active_mode(self):
        return self.get_text(OrderingTaxiLocators.MODE_ACTIVE)

    @property
    def car_price(self):
        return self.get_text(OrderingTaxiLocators.TEXT_CAR_PRICE)

    @property
    def taxi_price(self):
        return self.get_text(OrderingTaxiLocators.TEXT_TAXI_PRICE)

    def select_mode(self, mode):
        mode_locators = {
            "optimal": OrderingTaxiLocators.OPTIMAL_MODE,
            "fast": OrderingTaxiLocators.FAST_MODE,
            "custom": OrderingTaxiLocators.CUSTOM_MODE
        }
        self.click_element(mode_locators[mode])
        return self

    @property
    def all_tariffs_count(self):
        return self.get_elements_count(OrderingTaxiLocators.ALL_TARIFF_CARDS)

    @property
    def active_tariffs_count(self):
        return self.get_elements_count(OrderingTaxiLocators.ACTIVE_TARIFF_CARD)

    @property
    def active_tariff_name(self):
        active_card = self.wait.until(EC.visibility_of_element_located(
            OrderingTaxiLocators.ACTIVE_TARIFF_CARD))
        return self.get_child_text(active_card, OrderingTaxiLocators.TARIFF_TITLES)

    @property
    def all_tariff_names(self):
        return self.get_elements_texts(OrderingTaxiLocators.TARIFF_TITLES)

    def is_tariff_visible(self, tariff_name):
        locators = {
            "Рабочий": OrderingTaxiLocators.WORKER_TITLE,
            "Сонный": OrderingTaxiLocators.SLEEPY_TITLE,
            "Отпускной": OrderingTaxiLocators.VACATION_TITLE,
            "Разговорчивый": OrderingTaxiLocators.TALKATIVE_TITLE,
            "Утешительный": OrderingTaxiLocators.COMFORTING_TITLE,
            "Глянцевый": OrderingTaxiLocators.GLOSSY_TITLE
        }
        return self.is_element_visible(locators[tariff_name])

    def move_cursor_to_safe_zone(self):
        body = self.driver.find_element(By.TAG_NAME, "body")
        ActionChains(self.driver).move_to_element(body).pause(0.5).perform()

    def get_tooltip_text(self):
        return self.wait.until(EC.visibility_of_element_located(OrderingTaxiLocators.TOOLTIP_CONTENT)).text.strip()

    def verify_tariff_description(self, tariff_name):
        expected = OrderingTaxiLocators.EXPECTED_TEXTS[tariff_name]
        actual = self.get_tooltip_text()
        assert expected in actual, (
            f"Неверное описание тарифа '{tariff_name}'\n"
            f"Ожидалось: {expected}\n"
            f"Фактически: {actual}"
        )

    def move_cursor_to_field_from(self):
        field = self.wait.until(EC.presence_of_element_located(DrawingRouteLocators.FIELD_FROM))
        ActionChains(self.driver).move_to_element(field).pause(0.5).perform()

    def check_tariff_tooltip(self, tariff_name):
        try:
            self._select_tariff(tariff_name)
            button = self.wait.until(EC.element_to_be_clickable(self._get_locator(tariff_name, "button")))
            button.click()
            tooltip = self.wait.until(EC.visibility_of_element_located(self._get_locator(tariff_name, "tooltip")))
            actual_text = tooltip.find_element(*self._get_locator(tariff_name, "description")).text.strip()
            expected_text = OrderingTaxiLocators.EXPECTED_TEXTS[tariff_name]
            assert actual_text == expected_text, (
                f"Неверное описание для '{tariff_name}'\n"
                f"Ожидалось: '{expected_text}'\nПолучено: '{actual_text}'"
            )
            return True
        except Exception as e:
            raise Exception(f"Ошибка проверки тарифа '{tariff_name}': {str(e)}")
        finally:
            self._close_tooltip()

    def _get_tariff_locators(self, tariff_name):
        return {
            "Рабочий": {
                "button": OrderingTaxiLocators.WORKER_BUTTON,
                "tooltip": OrderingTaxiLocators.WORKER_TOOLTIP,
                "description": OrderingTaxiLocators.WORKER_DESCRIPTION
            },
            "Сонный": {
                "button": OrderingTaxiLocators.SLEEPY_BUTTON,
                "tooltip": OrderingTaxiLocators.SLEEPY_TOOLTIP,
                "description": OrderingTaxiLocators.SLEEPY_DESCRIPTION
            },
            "Отпускной": {
                "button": OrderingTaxiLocators.VACATION_BUTTON,
                "tooltip": OrderingTaxiLocators.VACATION_TOOLTIP,
                "description": OrderingTaxiLocators.VACATION_DESCRIPTION
            },
            "Разговорчивый": {
                "button": OrderingTaxiLocators.TALKATIVE_BUTTON,
                "tooltip": OrderingTaxiLocators.TALKATIVE_TOOLTIP,
                "description": OrderingTaxiLocators.TALKATIVE_DESCRIPTION
            },
            "Утешительный": {
                "button": OrderingTaxiLocators.COMFORTING_BUTTON,
                "tooltip": OrderingTaxiLocators.COMFORTING_TOOLTIP,
                "description": OrderingTaxiLocators.COMFORTING_DESCRIPTION
            },
            "Глянцевый": {
                "button": OrderingTaxiLocators.GLOSSY_BUTTON,
                "tooltip": OrderingTaxiLocators.GLOSSY_TOOLTIP,
                "description": OrderingTaxiLocators.GLOSSY_DESCRIPTION
            }
        }[tariff_name]

    def _scroll_to_and_click(self, element):
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        ActionChains(self.driver).move_to_element(element).click().perform()

    def _get_title_locator(self, tariff_name):
        return {
            "Рабочий": OrderingTaxiLocators.WORKER_TITLE,
            "Сонный": OrderingTaxiLocators.SLEEPY_TITLE,
            "Отпускной": OrderingTaxiLocators.VACATION_TITLE,
            "Разговорчивый": OrderingTaxiLocators.TALKATIVE_TITLE,
            "Утешительный": OrderingTaxiLocators.COMFORTING_TITLE,
            "Глянцевый": OrderingTaxiLocators.GLOSSY_TITLE
        }[tariff_name]

    def _select_tariff(self, tariff_name):
        title = self.wait.until(EC.element_to_be_clickable(self._get_locator(tariff_name, "title")))
        self.driver.execute_script("arguments[0].scrollIntoView();", title)
        title.click()

    def _close_tooltip(self):
        ActionChains(self.driver).send_keys("\ue00c").perform()

    def _get_locator(self, tariff_name, element_type):
        name_mapping = {
            "Рабочий": "WORKER",
            "Сонный": "SLEEPY",
            "Отпускной": "VACATION",
            "Разговорчивый": "TALKATIVE",
            "Утешительный": "COMFORTING",
            "Глянцевый": "GLOSSY"
        }
        attr_name = f"{name_mapping[tariff_name]}_{element_type.upper()}"
        return getattr(OrderingTaxiLocators, attr_name)

    def is_phone_field_visible(self):
        return self.is_element_visible(OrderingTaxiLocators.PHONE_LABEL)

    def is_payment_method_visible(self):
        return self.is_element_visible(OrderingTaxiLocators.PAYMENT_METHOD_LABEL)

    def is_driver_comment_visible(self):
        return self.is_element_visible(OrderingTaxiLocators.DRIVER_COMMENT_LABEL)

    def is_requirements_visible(self):
        return self.is_element_visible(OrderingTaxiLocators.REQUIREMENTS_HEADER)

    def toggle_laptop_table(self, enable=True):
        current_state = self.is_element_selected(OrderingTaxiLocators.TOGGLE_SWITCH)
        if current_state != enable:
            self.click_element(OrderingTaxiLocators.TOGGLE_SWITCH)

    def confirm_order(self):
        self.click_element(OrderingTaxiLocators.SUBMIT_BUTTON)

    def is_waiting_modal_visible(self):
        return self.is_element_visible(OrderingTaxiLocators.CLOSE_BUTTON)

    def scroll_and_click_requirements(self):
        requirements_button = self.wait.until(EC.element_to_be_clickable(OrderingTaxiLocators.REQUIREMENTS_HEADER))
        self.scroll_to_element(requirements_button)
        self.click_element(OrderingTaxiLocators.REQUIREMENTS_HEADER)
        return self

    def wait_for_order_number(self, timeout=45):
        return self.is_element_visible(OrderingTaxiLocators.ORDER_NUMBER)

    def extract_price_value(self, price_text):
        import re
        match = re.search(r'(\d+)', price_text)
        return match.group(1) if match else None
