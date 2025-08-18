from selenium.webdriver.common.by import By


class PreparingOrderTaxiLocators:
    OPTIMAL_MODE = (By.XPATH, "//div[@class='mode' and text()='Оптимальный']")
    FAST_MODE = (By.XPATH, "//div[@class='mode' and text()='Быстрый']")
    CUSTOM_MODE = (By.XPATH, "//div[@class='mode' and text()='Свой']")
    MODE_ACTIVE = (By.XPATH, "//div[contains(@class, 'mode active')]")

    TEXT_CAR_PRICE = (By.XPATH, "//div[@class='text' and contains(., 'Авто')]/following-sibling::div[@class='duration']")
    TEXT_TAXI_PRICE = (By.XPATH, "//div[@class='text' and contains(., 'Такси')]/following-sibling::div[@class='duration']")

    BUTTON_CALL_TAXI = (By.XPATH, "//button[@type='button' and contains(@class, 'button') and contains(@class, 'round') and text()='Вызвать такси']")
    BUTTON_BOOK = (By.XPATH, "//button[@class='button round' and text()='Забронировать']")
    DRIVE_TYPE = (By.XPATH, "//div[contains(@class, 'type') and contains(@class, 'drive')]/img[@class='type-icon']")