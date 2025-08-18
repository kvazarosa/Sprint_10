from selenium.webdriver.common.by import By


class OrderingTaxiLocators:
    OPTIMAL_MODE = (By.XPATH, "//div[@class='mode' and text()='Оптимальный']")
    FAST_MODE = (By.XPATH, "//div[@class='mode' and text()='Быстрый']")
    CUSTOM_MODE = (By.XPATH, "//div[@class='mode' and text()='Свой']")
    MODE_ACTIVE = (By.XPATH, "//div[contains(@class, 'mode active')]")

    TEXT_CAR_PRICE = (By.XPATH, "//div[@class='text' and contains(., 'Авто')]/following-sibling::div[@class='duration']")
    TEXT_TAXI_PRICE = (By.XPATH, "//div[@class='text' and contains(., 'Такси')]/following-sibling::div[@class='duration']")

    BUTTON_CALL_TAXI = (By.XPATH, "//button[@type='button' and contains(@class, 'button') and contains(@class, 'round') and text()='Вызвать такси']")
    BUTTON_BOOK = (By.XPATH, "//button[@class='button round' and text()='Забронировать']")
    DRIVE_TYPE = (By.XPATH, "//div[contains(@class, 'type') and contains(@class, 'drive')]/img[@class='type-icon']")

    WORKER_TITLE = (By.XPATH, "//div[@class='tcard-title' and text()='Рабочий']")
    SLEEPY_TITLE = (By.XPATH, "//div[@class='tcard-title' and text()='Сонный']")
    VACATION_TITLE = (By.XPATH, "//div[@class='tcard-title' and text()='Отпускной']")
    TALKATIVE_TITLE = (By.XPATH, "//div[@class='tcard-title' and text()='Разговорчивый']")
    COMFORTING_TITLE = (By.XPATH, "//div[@class='tcard-title' and text()='Утешительный']")
    GLOSSY_TITLE = (By.XPATH, "//div[@class='tcard-title' and text()='Глянцевый']")

    # Кнопки "i" (восклицательные знаки)
    WORKER_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-0']")
    SLEEPY_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-1']")
    VACATION_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-2']")
    TALKATIVE_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-3']")
    COMFORTING_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-4']")
    GLOSSY_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-5']")

    # Всплывающие окна (tooltips)
    WORKER_TOOLTIP = (By.ID, "tariff-card-0")
    SLEEPY_TOOLTIP = (By.ID, "tariff-card-1")
    VACATION_TOOLTIP = (By.ID, "tariff-card-2")
    TALKATIVE_TOOLTIP = (By.ID, "tariff-card-3")
    COMFORTING_TOOLTIP = (By.ID, "tariff-card-4")
    GLOSSY_TOOLTIP = (By.ID, "tariff-card-5")

    # Тексты описаний
    WORKER_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-0 .i-dPrefix")
    SLEEPY_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-1 .i-dPrefix")
    VACATION_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-2 .i-dPrefix")
    TALKATIVE_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-3 .i-dPrefix")
    COMFORTING_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-4 .i-dPrefix")
    GLOSSY_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-5 .i-dPrefix")

    # Ожидаемые тексты
    EXPECTED_TEXTS = {
        "Рабочий": "Для деловых особ, которых отвлекают",
        "Сонный": "Для тех, кто не выспался",
        "Отпускной": "Если пришла пора отдохнуть",
        "Разговорчивый": "Если мысли не выходят из головы",
        "Утешительный": "Если хочется свернуться калачиком",
        "Глянцевый": "Если нужно блистать"
    }

    ALL_TARIFF_CARDS = (By.CSS_SELECTOR, "div.tcard")
    ACTIVE_TARIFF_CARD = (By.CSS_SELECTOR, "div.tcard.active")
    TARIFF_TITLES = (By.CSS_SELECTOR, "div.tcard-title")
    TARIFF_ACTIVE_BUTTON = (By.XPATH, "//button[contains(@class, 'tcard-i') and contains(@class, 'active') and @data-for='tariff-card-1' and @data-tip='true']")
    TARIFF_INFO_ICONS = (By.CSS_SELECTOR, "button.i-button.tcard-i[data-tip='true']")
    TOOLTIP_CONTENT = (By.CSS_SELECTOR, "div[role='tooltip']")

    TARIFF_DESCRIPTIONS = {
        "Рабочий": "Для деловых особ, которых отвлекают",
        "Сонный": "Для тех, кто не выспался",
        "Отпускной": "Если пришла пора отдохнуть",
        "Разговорчивый": "Если мысли не выходят из головы",
        "Утешительный": "Если хочется свернуться калачиком",
        "Глянцевый": "Если нужно блистать"
    }

    REQUIREMENTS_FOR_THE_ORDER = (By.XPATH, "//div[@class='reqs-head' and text()='Требования к заказу']")
