from selenium.webdriver.common.by import By
from data import Messages


class RenderingBlockLocators:
    ROUTE_SELECTION_BLOCK = (By.CSS_SELECTOR, "div.workflow-subcontainer")
    SAME_ADDRESS_MESSAGE = (By.XPATH, f"//div[contains(text(), '{Messages.SAME_ADDRESS_ROUTE}')]")
    ANY_TEXT_ELEMENT = (By.XPATH, "//*[contains(text(), '{}')]")