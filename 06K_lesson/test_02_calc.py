from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest


@pytest.fixture
def browser():
    # Используем Google Chrome как указано в задании
    driver = webdriver.Chrome(service=ChromeService(ChromeDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_slow_calculator(browser):
    # 1. Открываем страницу
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # 2. В поле ввода #delay вводим значение 45
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()  # Очищаем поле, если там есть значение по умолчанию
    delay_input.send_keys("45")
    
    # 3. Нажимаем на кнопки: 7 + 8 =
    # Кнопка 7
    button_7 = browser.find_element(By.XPATH, "//span[text()='7']")
    button_7.click()
    
    # Кнопка +
    button_plus = browser.find_element(By.XPATH, "//span[text()='+']")
    button_plus.click()
    
    # Кнопка 8
    button_8 = browser.find_element(By.XPATH, "//span[text()='8']")
    button_8.click()
    
    # Кнопка =
    button_equals = browser.find_element(By.XPATH, "//span[text()='=']")
    button_equals.click()
    
    # 4. Проверяем, что в окне отобразится результат 15 через 45 секунд
    # Ждем до 46 секунд, чтобы уложиться в таймаут
    wait = WebDriverWait(browser, 46)
    
    # Ждем, когда результат станет равным "15"
    result = wait.until(
        EC.text_to_be_present_in_element((By.CSS_SELECTOR, ".screen"), "15")
    )
    
    # Получаем фактический результат из элемента
    result_element = browser.find_element(By.CSS_SELECTOR, ".screen")
    actual_result = result_element.text
    
    # Проверяем через assert
    assert actual_result == "15", f"Ожидаемый результат: 15, Фактический результат: {actual_result}"
    
    print(f"Результат отобразился корректно: {actual_result}")


def test_slow_calculator_alternative(browser):
    """Альтернативная версия с более точной проверкой времени"""
    # 1. Открываем страницу
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/slow-calculator.html")
    
    # 2. В поле ввода #delay вводим значение 45
    delay_input = browser.find_element(By.CSS_SELECTOR, "#delay")
    delay_input.clear()
    delay_input.send_keys("45")
    
    # Запоминаем начальное время
    import time
    start_time = time.time()
    
    # 3. Нажимаем на кнопки: 7 + 8 =
    buttons_to_click = ["7", "+", "8", "="]
    
    for button_text in buttons_to_click:
        button = browser.find_element(By.XPATH, f"//span[text()='{button_text}']")
        button.click()
    
    # 4. Ждем появления результата
    wait = WebDriverWait(browser, 50)
    
    # Проверяем, что результат появился и равен 15
    def result_is_15(driver):
        result_element = driver.find_element(By.CSS_SELECTOR, ".screen")
        return result_element.text == "15"
    
    # Ждем до 50 секунд
    wait.until(result_is_15)
    
    # Запоминаем время окончания
    end_time = time.time()
    elapsed_time = end_time - start_time
    
    # Проверяем, что результат верный
    result_element = browser.find_element(By.CSS_SELECTOR, ".screen")
    actual_result = result_element.text
    
    # Проверяем через assert
    assert actual_result == "15", f"Ожидаемый результат: 15, Фактический результат: {actual_result}"
    
    # Дополнительная проверка: время выполнения примерно 45 секунд
    print(f"Время выполнения: {elapsed_time:.2f} секунд")
    print(f"Результат отобразился корректно: {actual_result}")
    
    # Нестрогая проверка времени (ожидаем примерно 45 секунд с допуском)
    # 45 секунд задержка + время на нажатия кнопок ≈ 46-47 секунд
    assert elapsed_time > 44, f"Выполнение заняло всего {elapsed_time:.2f} секунд, ожидалось более 44 секунд"
    assert elapsed_time < 50, f"Выполнение заняло {elapsed_time:.2f} секунд, что слишком долго"


if __name__ == "__main__":
    pytest.main([__file__, "-v"])