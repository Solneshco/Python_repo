import unittest
import time
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.calculator_page import CalculatorPage


class CalculatorTest(unittest.TestCase):
    def setUp(self):
        """Настройка перед каждым тестом"""
        print("=" * 50)
        print("Настройка драйвера...")

        try:
            # Используем webdriver-manager для автоматической загрузки ChromeDriver
            service = Service(ChromeDriverManager().install())
            self.driver = webdriver.Chrome(service=service)
            print("✓ ChromeDriver успешно загружен через webdriver-manager")
        except Exception as e:
            print(f"Ошибка webdriver-manager: {e}")
            print("Пытаюсь использовать стандартный ChromeDriver...")
            self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.get(
            "https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html"
        )
        self.calculator_page = CalculatorPage(self.driver)
        print("✓ Страница калькулятора загружена")

    def test_slow_calculator(self):
        """Тест калькулятора с задержкой 45 секунд"""
        print("\n" + "=" * 50)
        print("Запуск теста: 7 + 8 с задержкой 45 секунд")
        print("=" * 50)

        # 1. Ввод значения задержки
        print("1. Устанавливаю задержку: 45 секунд")
        self.calculator_page.set_delay("45")

        # 2. Выполнение операции: 7 + 8
        print("2. Выполняю операцию: 7 + 8 =")
        self.calculator_page.click_button_7()
        self.calculator_page.click_button_plus()
        self.calculator_page.click_button_8()
        self.calculator_page.click_button_equals()

        # 3. Ожидание и проверка результата
        print("3. Ожидаю 45 секунд...")
        print("   (тест будет выполняться около 45 секунд)")
        start_time = time.time()

        result = self.calculator_page.get_result_with_explicit_wait()

        end_time = time.time()
        elapsed_time = end_time - start_time
        print(f"✓ Ожидание завершено за {elapsed_time:.1f} секунд")

        # 4. Проверка результата
        print(f"4. Проверяю результат...")
        print(f"   Ожидаемый результат: 15")
        print(f"   Фактический результат: {result}")

        self.assertEqual("15", result, "Результат вычисления должен быть 15")
        print("✓ ТЕСТ УСПЕШНО ПРОЙДЕН!")

    def tearDown(self):
        """Очистка после каждого теста"""
        print("\n" + "=" * 50)
        print("Завершение теста...")
        self.driver.quit()
        print("Браузер закрыт")
        print("=" * 50)


if __name__ == "__main__":
    # Запуск теста с максимальной детализацией
    unittest.main(verbosity=2)