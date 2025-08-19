from selenium.webdriver.common.by import By


class DrawingRouteLocators:
    FIELD_FROM = (By.ID, "from")
    FIELD_WHERE = (By.ID, "to")
    KHAMOVNICHESKY = (By.XPATH, "//ymaps[contains(., 'Хамовнический Вал, 34')]")
    ZUBOVSKY = (By.XPATH, "//ymaps[contains(., 'Зубовский бульвар, 37')]")
