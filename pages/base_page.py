from selenium.webdriver import ActionChains
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 10)

    def input_address(self, locator, text):
        element = self.wait.until(EC.visibility_of_element_located(locator))
        element.clear()
        element.send_keys(text)

    def is_point_visible(self, locator):
        try:
            return self.wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def click_element(self, locator):
        element = self.wait.until(EC.element_to_be_clickable(locator))
        element.click()
        return self

    def is_element_visible(self, locator, timeout=10):
        try:
            wait = WebDriverWait(self.driver, timeout)
            return wait.until(EC.visibility_of_element_located(locator)).is_displayed()
        except:
            return False

    def get_text(self, locator):
        return self.wait.until(EC.visibility_of_element_located(locator)).text

    def get_elements_count(self, locator):
        return len(self.wait.until(EC.visibility_of_all_elements_located(locator)))

    def get_elements_texts(self, locator):
        return [el.text for el in self.wait.until(EC.visibility_of_all_elements_located(locator))]

    def get_child_text(self, parent_element, child_locator):
        return parent_element.find_element(*child_locator).text

    def hover_element(self, element):
        """Наводит курсор на элемент"""
        ActionChains(self.driver).move_to_element(element).perform()
        return self

    def scroll_to_element(self, element):
        """Прокручивает страницу к элементу"""
        self.driver.execute_script(
            "arguments[0].scrollIntoView({block: 'center'});",
            element
        )
        return self

    def is_element_selected(self, locator):
        return self.wait.until(EC.presence_of_element_located(locator)).is_selected()
