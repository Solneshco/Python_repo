from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class CalculatorPage:
    def __init__(self, driver):
        self.driver = driver
        self.delay_input = (By.CSS_SELECTOR, "#delay")
        self.result_display = (By.CSS_SELECTOR, ".screen")

    def open(self, url):
        self.driver.get(url)
        return self

    def set_delay(self, seconds):
        delay_element = self.driver.find_element(*self.delay_input)
        delay_element.clear()
        delay_element.send_keys(str(seconds))

    def click_button(self, button_text):
        button_locator = (By.XPATH, f"//span[text()='{button_text}']")
        button = self.driver.find_element(*button_locator)
        button.click()

    def get_display_text(self):
        return self.driver.find_element(*self.result_display).text

    def wait_for_result(self, expected_result, timeout=50):
        wait = WebDriverWait(self.driver, timeout)
        wait.until(
            EC.text_to_be_present_in_element(self.result_display, expected_result)
        )
        return self.get_display_text()

    def calculate(self, expression):
        for char in expression:
            self.click_button(char)
