import pytest
from selenium import webdriver
from calculator_page import CalculatorPage


class TestCalculator:
    def setup_method(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def teardown_method(self):
        self.driver.quit()

    def test_calculator_with_delay(self):
        calculator_page = CalculatorPage(self.driver)

        calculator_page.open(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )

        calculator_page.set_delay(45)

        calculator_page.calculate("7+8=")

        result = calculator_page.wait_for_result("15", timeout=50)

        assert result == "15", f"Ожидалось 15, но получено {result}"
