from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.firefox import GeckoDriverManager
from selenium.webdriver.firefox.service import Service as FirefoxService
import pytest


@pytest.fixture
def browser():
    # Используем FireFox как указано в задании
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    yield driver
    driver.quit()


def test_shopping_cart_total():
    # Создаем драйвер внутри теста, чтобы точно закрыть его после assert
    driver = webdriver.Firefox(service=FirefoxService(GeckoDriverManager().install()))
    driver.maximize_window()
    
    try:
        # 1. Открываем сайт магазина
        driver.get("https://www.saucedemo.com/")
        
        # 2. Авторизуемся как пользователь standard_user
        username_input = driver.find_element(By.ID, "user-name")
        username_input.send_keys("standard_user")
        
        password_input = driver.find_element(By.ID, "password")
        password_input.send_keys("secret_sauce")
        
        login_button = driver.find_element(By.ID, "login-button")
        login_button.click()
        
        # Ждем загрузки страницы с товарами
        wait = WebDriverWait(driver, 10)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
        
        # 3. Добавляем в корзину товары:
        # Sauce Labs Backpack
        backpack_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
        backpack_add_button.click()
        
        # Sauce Labs Bolt T-Shirt
        tshirt_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
        tshirt_add_button.click()
        
        # Sauce Labs Onesie
        onesie_add_button = driver.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
        onesie_add_button.click()
        
        # 4. Переходим в корзину
        cart_icon = driver.find_element(By.CLASS_NAME, "shopping_cart_link")
        cart_icon.click()
        
        # Ждем загрузки страницы корзины
        wait.until(EC.presence_of_element_located((By.ID, "checkout")))
        
        # 5. Нажимаем Checkout
        checkout_button = driver.find_element(By.ID, "checkout")
        checkout_button.click()
        
        # 6. Заполняем форму своими данными
        wait.until(EC.presence_of_element_located((By.ID, "first-name")))
        
        # Имя
        first_name_input = driver.find_element(By.ID, "first-name")
        first_name_input.send_keys("Иван")
        
        # Фамилия
        last_name_input = driver.find_element(By.ID, "last-name")
        last_name_input.send_keys("Петров")
        
        # Почтовый индекс
        postal_code_input = driver.find_element(By.ID, "postal-code")
        postal_code_input.send_keys("123456")
        
        # 7. Нажимаем кнопку Continue
        continue_button = driver.find_element(By.ID, "continue")
        continue_button.click()
        
        # 8. Читаем со страницы итоговую стоимость (Total)
        wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
        
        total_element = driver.find_element(By.CLASS_NAME, "summary_total_label")
        total_text = total_element.text
        
        # Извлекаем сумму из текста (формат: "Total: $58.29")
        total_amount = total_text.split("$")[1]
        
        # 10. Проверяем, что итоговая сумма равна $58.29
        assert total_amount == "58.29", f"Ожидаемая сумма: $58.29, Фактическая сумма: ${total_amount}"
        
        print(f"Итоговая сумма корректна: ${total_amount}")
        
    finally:
        # 9. Закрываем браузер
        driver.quit()


def test_shopping_cart_total_with_fixture(browser):
    """Тот же тест, но с использованием фикстуры browser"""
    # 1. Открываем сайт магазина
    browser.get("https://www.saucedemo.com/")
    
    # 2. Авторизуемся как пользователь standard_user
    username_input = browser.find_element(By.ID, "user-name")
    username_input.send_keys("standard_user")
    
    password_input = browser.find_element(By.ID, "password")
    password_input.send_keys("secret_sauce")
    
    login_button = browser.find_element(By.ID, "login-button")
    login_button.click()
    
    # Ждем загрузки страницы с товарами
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    
    # 3. Добавляем в корзину товары:
    # Sauce Labs Backpack
    backpack_add_button = browser.find_element(By.ID, "add-to-cart-sauce-labs-backpack")
    backpack_add_button.click()
    
    # Sauce Labs Bolt T-Shirt
    tshirt_add_button = browser.find_element(By.ID, "add-to-cart-sauce-labs-bolt-t-shirt")
    tshirt_add_button.click()
    
    # Sauce Labs Onesie
    onesie_add_button = browser.find_element(By.ID, "add-to-cart-sauce-labs-onesie")
    onesie_add_button.click()
    
    # 4. Переходим в корзину
    cart_icon = browser.find_element(By.CLASS_NAME, "shopping_cart_link")
    cart_icon.click()
    
    # Ждем загрузки страницы корзины
    wait.until(EC.presence_of_element_located((By.ID, "checkout")))
    
    # 5. Нажимаем Checkout
    checkout_button = browser.find_element(By.ID, "checkout")
    checkout_button.click()
    
    # 6. Заполняем форму своими данными
    wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    
    # Имя
    first_name_input = browser.find_element(By.ID, "first-name")
    first_name_input.send_keys("Иван")
    
    # Фамилия
    last_name_input = browser.find_element(By.ID, "last-name")
    last_name_input.send_keys("Петров")
    
    # Почтовый индекс
    postal_code_input = browser.find_element(By.ID, "postal-code")
    postal_code_input.send_keys("123456")
    
    # 7. Нажимаем кнопку Continue
    continue_button = browser.find_element(By.ID, "continue")
    continue_button.click()
    
    # 8. Читаем со страницы итоговую стоимость (Total)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    
    total_element = browser.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    
    # Извлекаем сумму из текста (формат: "Total: $58.29")
    total_amount = total_text.split("$")[1]
    
    # 10. Проверяем, что итоговая сумма равна $58.29
    assert total_amount == "58.29", f"Ожидаемая сумма: $58.29, Фактическая сумма: ${total_amount}"
    
    print(f"Итоговая сумма корректна: ${total_amount}")


def test_shopping_cart_total_clean(browser):
    """Оптимизированная версия теста с более чистыми локаторами"""
    # 1. Открываем сайт
    browser.get("https://www.saucedemo.com/")
    
    # 2. Авторизация
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    # Ждем загрузки
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    
    # 3. Добавляем товары в корзину
    products_to_add = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt", 
        "sauce-labs-onesie"
    ]
    
    for product_id in products_to_add:
        add_button = browser.find_element(By.ID, f"add-to-cart-{product_id}")
        add_button.click()
    
    # 4. Переходим в корзину
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    
    # 5. Нажимаем Checkout
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    
    # 6. Заполняем форму
    wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    
    browser.find_element(By.ID, "first-name").send_keys("Иван")
    browser.find_element(By.ID, "last-name").send_keys("Петров")
    browser.find_element(By.ID, "postal-code").send_keys("123456")
    
    # 7. Продолжаем
    browser.find_element(By.ID, "continue").click()
    
    # 8. Получаем итоговую сумму
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label")))
    
    total_text = browser.find_element(By.CLASS_NAME, "summary_total_label").text
    
    # Проверяем полный текст
    expected_text = "Total: $58.29"
    assert total_text == expected_text, f"Ожидалось: {expected_text}, Получено: {total_text}"
    
    print(f"Проверка пройдена: {total_text}")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])