import pytest
from selenium import webdriver
from pages.login_page import LoginPage

class TestSauceDemoPurchase:
    @pytest.fixture
    def driver(self):
        # Создаем драйвер Firefox
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
        # Закрываем браузер после теста
        driver.quit()
    
    def test_total_price_should_be_58_29(self, driver):
        # Шаг 1: Авторизация
        main_page = (LoginPage(driver)
                    .open()
                    .enter_username("standard_user")
                    .enter_password("secret_sauce")
                    .click_login())
        
        # Шаг 2: Добавление товаров
        (main_page
         .add_item_to_cart("Sauce Labs Backpack")
         .add_item_to_cart("Sauce Labs Bolt T-Shirt")
         .add_item_to_cart("Sauce Labs Onesie"))
        
        # Шаг 3: Переход в корзину и оформление
        cart_page = main_page.go_to_cart()
        
        checkout_step_one = cart_page.click_checkout()
        
        checkout_step_two = (checkout_step_one
                            .fill_shipping_info("Иван", "Петров", "123456")
                            .click_continue())
        
        # Шаг 4: Получение и проверка итоговой суммы
        total_text = checkout_step_two.get_total_price()
        # Извлекаем число из строки "Total: $58.29"
        total_value = total_text.replace("Total: $", "")
        
        assert total_value == "58.29", \
            f"Ожидалась сумма $58.29, но получена ${total_value}"
        print(f"Тест пройден! Итоговая сумма: ${total_value}")