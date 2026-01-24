from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager
from selenium.webdriver.chrome.service import Service as ChromeService
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Chrome(
        service=ChromeService(ChromeDriverManager().install())
    )
    driver.maximize_window()
    yield driver
    driver.quit()


def test_01_form(browser):
    browser.get("https://www.saucedemo.com/")
    
    browser.find_element(By.ID, "user-name").send_keys("standard_user")
    browser.find_element(By.ID, "password").send_keys("secret_sauce")
    browser.find_element(By.ID, "login-button").click()
    
    wait = WebDriverWait(browser, 10)
    wait.until(EC.presence_of_element_located((By.CLASS_NAME, "inventory_item")))
    
    products_to_add = [
        "sauce-labs-backpack",
        "sauce-labs-bolt-t-shirt",
        "sauce-labs-onesie"
    ]
    
    for product_id in products_to_add:
        add_button = browser.find_element(
            By.ID, f"add-to-cart-{product_id}"
        )
        add_button.click()
    
    browser.find_element(By.CLASS_NAME, "shopping_cart_link").click()
    wait.until(EC.element_to_be_clickable((By.ID, "checkout"))).click()
    wait.until(EC.presence_of_element_located((By.ID, "first-name")))
    
    browser.find_element(By.ID, "first-name").send_keys("Иван")
    browser.find_element(By.ID, "last-name").send_keys("Петров")
    browser.find_element(By.ID, "postal-code").send_keys("123456")
    browser.find_element(By.ID, "continue").click()
    
    wait.until(
        EC.presence_of_element_located((By.CLASS_NAME, "summary_total_label"))
    )
    
    total_element = browser.find_element(By.CLASS_NAME, "summary_total_label")
    total_text = total_element.text
    
    expected_text = "Total: $58.29"
    assert total_text == expected_text, (
        f"Ожидаемый текст: {expected_text}, "
        f"Фактический текст: {total_text}"
    )


if __name__ == "__main__":
    pytest.main([__file__, "-v"])