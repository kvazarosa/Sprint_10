from selenium import webdriver
from data import Urls
import pytest
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from locators.drawing_route_locators import DrawingRouteLocators


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
