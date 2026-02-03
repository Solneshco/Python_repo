import pytest
import allure
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager

from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage


class TestSauceDemo:
    """Тесты для интернет-магазина Sauce Demo."""

    def setup_method(self):
        """
        Настройка перед каждым тестом.
        """
        with allure.step("Инициализация WebDriver"):
            # Вариант 1: Использование webdriver-manager (автоматическая загрузка драйвера)
            self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))
            # Вариант 2: Если драйвер уже установлен в PATH
            # self.driver = webdriver.Chrome()
            self.driver.maximize_window()
            self.driver.implicitly_wait(5)

    def teardown_method(self):
        """
        Очистка после каждого теста.
        """
        with allure.step("Закрытие браузера"):
            self.driver.quit()

    @allure.title("Проверка итоговой суммы при оформлении заказа")
    @allure.description("""
    Тест проверяет корректность расчета итоговой суммы
    при добавлении трех товаров в корзину и оформлении заказа.
    
    Тестовые данные:
    - Пользователь: standard_user
    - Товары: Sauce Labs Backpack, Sauce Labs Bolt T-Shirt, Sauce Labs Onesie
    - Ожидаемая итоговая сумма: $58.29
    """)
    @allure.feature("Оформление заказа")
    @allure.severity(allure.severity_level.CRITICAL)
    def test_checkout_total_amount(self):
        """
        Проверяет корректность расчета итоговой суммы при оформлении заказа.
        """
        # Инициализация объектов страниц
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        checkout_overview_page = CheckoutOverviewPage(self.driver)

        # 1. Открыть сайт магазина
        with allure.step("Открыть сайт магазина"):
            login_page.open()

        # 2. Авторизоваться как пользователь standard_user
        with allure.step("Авторизоваться как пользователь standard_user"):
            login_page.login("standard_user", "secret_sauce")

        # Проверяем, что авторизация прошла успешно
        with allure.step("Проверить успешную авторизацию"):
            assert inventory_page.get_page_title() == "Products", \
                "Ожидался заголовок 'Products' после авторизации"

        # 3. Добавить товары в корзину
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]
        
        with allure.step(f"Добавить товары в корзину: {', '.join(products_to_add)}"):
            for product in products_to_add:
                inventory_page.add_to_cart(product)

        # Проверяем, что в корзине 3 товара
        with allure.step("Проверить количество товаров в корзине"):
            cart_count = inventory_page.get_cart_count()
            assert cart_count == 3, f"Ожидалось 3 товара в корзине, но найдено {cart_count}"

        # 4. Перейти в корзину
        with allure.step("Перейти в корзину"):
            inventory_page.go_to_cart()

        # Проверяем, что мы на странице корзины
        with allure.step("Проверить, что открыта страница корзины"):
            cart_title = cart_page.get_page_title()
            assert cart_title == "Your Cart", \
                f"Ожидался заголовок 'Your Cart', но получен '{cart_title}'"

        # Проверяем, что в корзине нужные товары
        with allure.step("Проверить наличие добавленных товаров в корзине"):
            cart_items = cart_page.get_cart_item_names()
            for product in products_to_add:
                assert product in cart_items, f"Товар {product} отсутствует в корзине"

        # 5. Нажать кнопку Checkout
        with allure.step("Нажать кнопку Checkout"):
            cart_page.click_checkout()

        # Проверяем, что мы на странице оформления заказа
        with allure.step("Проверить, что открыта страница оформления заказа"):
            checkout_title = checkout_page.get_page_title()
            assert checkout_title == "Checkout: Your Information", \
                f"Ожидался заголовок 'Checkout: Your Information', но получен '{checkout_title}'"

        # 6. Заполнить форму своими данными
        with allure.step("Заполнить форму оформления заказа"):
            checkout_page.fill_checkout_form("Иван", "Иванов", "123456")
            checkout_page.click_continue()

        # 7. Проверить итоговую стоимость
        with allure.step("Проверить, что открыта страница обзора заказа"):
            overview_title = checkout_overview_page.get_page_title()
            assert overview_title == "Checkout: Overview", \
                f"Ожидался заголовок 'Checkout: Overview', но получен '{overview_title}'"

        total_text = checkout_overview_page.get_total_text()
        total_value = checkout_overview_page.get_total()
        
        with allure.step(f"Проверить итоговую сумму: {total_text}"):
            print(f"Итоговая сумма: {total_text}")
            assert total_value == 58.29, f"Ожидалось $58.29, но получено ${total_value}"

        # Дополнительные проверки (опционально)
        with allure.step("Проверить детализацию суммы"):
            item_total = checkout_overview_page.get_item_total()
            tax = checkout_overview_page.get_tax()
            print(f"Сумма товаров: ${item_total}")
            print(f"Налог: ${tax}")
            
            # Проверяем, что сумма товаров + налог = итоговая сумма
            calculated_total = round(item_total + tax, 2)
            assert calculated_total == total_value, \
                f"Сумма товаров (${item_total}) + налог (${tax}) = ${calculated_total}, " \
                f"но итоговая сумма = ${total_value}"