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

    WORKER_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-0']")
    SLEEPY_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-1']")
    VACATION_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-2']")
    TALKATIVE_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-3']")
    COMFORTING_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-4']")
    GLOSSY_BUTTON = (By.CSS_SELECTOR, "button.tcard-i[data-for='tariff-card-5']")

    WORKER_TOOLTIP = (By.ID, "tariff-card-0")
    SLEEPY_TOOLTIP = (By.ID, "tariff-card-1")
    VACATION_TOOLTIP = (By.ID, "tariff-card-2")
    TALKATIVE_TOOLTIP = (By.ID, "tariff-card-3")
    COMFORTING_TOOLTIP = (By.ID, "tariff-card-4")
    GLOSSY_TOOLTIP = (By.ID, "tariff-card-5")

    WORKER_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-0 .i-dPrefix")
    SLEEPY_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-1 .i-dPrefix")
    VACATION_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-2 .i-dPrefix")
    TALKATIVE_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-3 .i-dPrefix")
    COMFORTING_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-4 .i-dPrefix")
    GLOSSY_DESCRIPTION = (By.CSS_SELECTOR, "#tariff-card-5 .i-dPrefix")

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

    REQUIREMENTS_FOR_THE_ORDER = (By.XPATH, "//div[@class='reqs-head' and text()='Требования к заказу']")
    PHONE_LABEL = (By.XPATH, "//div[contains(@class, 'np-text') and text()='Телефон']")
    PAYMENT_METHOD_LABEL = (By.XPATH, "//div[@class='pp-text' and text()='Способ оплаты']")
    DRIVER_COMMENT_LABEL = (By.XPATH, "//label[@for='comment' and @class='label' and contains(text(), 'Комментарий водителю')]")
    REQUIREMENTS_HEADER = (By.XPATH, "//div[@class='reqs-head' and text()='Требования к заказу']")
    TOGGLE_SWITCH = (By.XPATH, "//span[contains(@class, 'slider') and contains(@class, 'round')]")
    SUBMIT_BUTTON = (By.XPATH, "//span[@class='smart-button-main' and text()='Ввести номер и заказать']")
    CLOSE_BUTTON = (By.XPATH, "//button[@class='order-button' and contains(.//img/@src, 'plus')]")
    ORDER_BODY = (By.XPATH, "//div[@class='order-body']")
    ORDER_NUMBER = (By.CSS_SELECTOR, "div.order-number")
    TAXI_PRICE = (By.XPATH, "//div[@class='text' and text()='Такси ~ 181 руб.']")
    BURGER_MENU_BUTTON = (By.XPATH, "//button[@class='order-button' and .//img[@alt='burger']]")
    ORDER_PRICE = (By.XPATH, "//div[contains(@class, 'o-d-sh') and contains(text(), 'Стоимость')]")
    DETAILS_BUTTON = (By.XPATH, "//button[contains(text(), 'Детали')]")
