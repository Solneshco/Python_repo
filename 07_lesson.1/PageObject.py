from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(driver, 60)

        # Локаторы
        self.delay_field = (By.CSS_SELECTOR, "#delay")
        self.button_7 = (By.CSS_SELECTOR, "[data-keys='7']")
        self.button_plus = (By.CSS_SELECTOR, "[data-keys='+']")
        self.button_8 = (By.CSS_SELECTOR, "[data-keys='8']")
        self.button_equals = (By.CSS_SELECTOR, "[data-keys='=']")
        self.result_screen = (By.CSS_SELECTOR, ".screen")

    def set_delay(self, delay):
        """Ввести значение задержки"""
        element = self.driver.find_element(*self.delay_field)
        element.clear()
        element.send_keys(delay)

    def click_button_7(self):
        """Нажать кнопку 7"""
        self.driver.find_element(*self.button_7).click()

    def click_button_plus(self):
        """Нажать кнопку +"""
        self.driver.find_element(*self.button_plus).click()

    def click_button_8(self):
        """Нажать кнопку 8"""
        self.driver.find_element(*self.button_8).click()

    def click_button_equals(self):
        """Нажать кнопку ="""
        self.driver.find_element(*self.button_equals).click()

    def wait_and_get_result(self):
        self.wait.until(
        EC.text_to_be_present_in_element(self.result_screen, "15")
    )
        return self.driver.find_element(*self.result_screen).text