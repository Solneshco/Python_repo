import pytest
from selenium import webdriver
from selenium.webdriver.common.by import By
from pages.login_page import LoginPage


class TestSauceDemoPurchase:
    @pytest.fixture
    def driver(self):
        """Фикстура для создания драйвера"""
        # Создаем драйвер Firefox
        driver = webdriver.Firefox()
        driver.maximize_window()
        yield driver
        # Закрываем браузер после теста
        driver.quit()

    def test_total_price_should_be_58_29(self, driver):
        """Тест проверки итоговой суммы покупки"""
        print("\n" + "=" * 50)
        print("Запуск теста: проверка суммы покупки $58.29")
        print("=" * 50)

        # Шаг 1: Авторизация
        print("1. Авторизация...")
        login_page = LoginPage(driver)
        
        main_page = (
            login_page
            .open()
            .enter_username("standard_user")
            .enter_password("secret_sauce")
            .click_login()
        )
        print("✓ Авторизация прошла успешно")

        # Шаг 2: Добавление товаров в корзину
        print("2. Добавление товаров в корзину...")
        (
            main_page
            .add_item_to_cart("Sauce Labs Backpack")
            .add_item_to_cart("Sauce Labs Bolt T-Shirt")
            .add_item_to_cart("Sauce Labs Onesie")
        )
        print("✓ Товары добавлены в корзину")

        # Шаг 3: Переход в корзину
        print("3. Переход в корзину...")
        cart_page = main_page.go_to_cart()
        print("✓ Корзина открыта")

        # Шаг 4: Начало оформления заказа
        print("4. Начало оформления заказа...")
        checkout_step_one = cart_page.click_checkout()
        print("✓ Оформление заказа начато")

        # Шаг 5: Заполнение информации о доставке
        print("5. Заполнение информации о доставке...")
        checkout_step_two = (
            checkout_step_one
            .fill_shipping_info("Иван", "Петров", "123456")
            .click_continue()
        )
        print("✓ Информация о доставке заполнена")

        # Шаг 6: Проверка итоговой суммы
        print("6. Проверка итоговой суммы...")
        total_text = checkout_step_two.get_total_price()
        print(f"   Получен текст: '{total_text}'")
        
        # Извлекаем число из строки "Total: $58.29"
        total_value = total_text.replace("Total: $", "")
        print(f"   Извлеченная сумма: ${total_value}")

        # Проверка результата
        assert total_value == "58.29", (
            f"Ожидалась сумма $58.29, но получена ${total_value}"
        )
        
        print("\n" + "=" * 50)
        print("✓ ТЕСТ УСПЕШНО ПРОЙДЕН!")
        print(f"Итоговая сумма: ${total_value}")
        print("=" * 50)


if __name__ == "__main__":
    # Запуск теста напрямую (для отладки)
    print("Запуск теста напрямую...")
    test = TestSauceDemoPurchase()
    
    # Создаем драйвер для прямого запуска
    driver = webdriver.Firefox()
    driver.maximize_window()
    
    try:
        test.test_total_price_should_be_58_29(driver)
    except Exception as e:
        print(f"Ошибка при выполнении теста: {e}")
        import traceback
        traceback.print_exc()
    finally:
        driver.quit()