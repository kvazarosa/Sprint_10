from selenium import webdriver
from data import Urls
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.drawing_route_locators import DrawingRouteLocators
from locators.preparing_order_taxi_locators import PreparingOrderTaxiLocators
from pages.preparing_order_taxi_page import PreparingOrderTaxiPage
from locators.ordering_taxi_locators import OrderingTaxiLocators


@pytest.fixture
def driver():
    driver = webdriver.Chrome()
    driver.maximize_window()
    driver.get(Urls.HOME_URL)
    yield driver
    driver.quit()


@pytest.fixture
def default_route(driver):
    driver.find_element(*DrawingRouteLocators.FIELD_FROM).send_keys("Хамовнический Вал, 34")
    driver.find_element(*DrawingRouteLocators.FIELD_WHERE).send_keys("Зубовский бульвар, 37")
    WebDriverWait(driver, 10).until(EC.visibility_of_element_located(DrawingRouteLocators.KHAMOVNICHESKY))


@pytest.fixture
def taxi_order_created(driver, default_route):
    page = PreparingOrderTaxiPage(driver)
    page.click_element(PreparingOrderTaxiLocators.BUTTON_CALL_TAXI)
    WebDriverWait(driver, 15).until(EC.visibility_of_element_located(OrderingTaxiLocators.REQUIREMENTS_FOR_THE_ORDER))
    yield driver

@pytest.fixture(params=[
    "Рабочий",
    "Сонный",
    "Отпускной",
    "Разговорчивый",
    "Утешительный",
    "Глянцевый"
], ids=lambda x: f"Тариф: {x}")
def tariff_name(request):
    return request.param