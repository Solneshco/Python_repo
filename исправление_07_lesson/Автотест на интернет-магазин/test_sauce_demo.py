import pytest
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from webdriver_manager.chrome import ChromeDriverManager
from pages.login_page import LoginPage
from pages.inventory_page import InventoryPage
from pages.cart_page import CartPage
from pages.checkout_page import CheckoutPage
from pages.checkout_overview_page import CheckoutOverviewPage


class TestSauceDemo:
    def setup_method(self):
        """Настройка перед каждым тестом"""
        # Вариант 1: Использование webdriver-manager (автоматическая загрузка драйвера)
        self.driver = webdriver.Chrome(service=Service(ChromeDriverManager().install()))

        # Вариант 2: Если драйвер уже установлен в PATH
        # self.driver = webdriver.Chrome()

        self.driver.maximize_window()
        self.driver.implicitly_wait(5)

    def teardown_method(self):
        """Очистка после каждого теста"""
        self.driver.quit()

    def test_checkout_total_amount(self):
        # Инициализация объектов страниц
        login_page = LoginPage(self.driver)
        inventory_page = InventoryPage(self.driver)
        cart_page = CartPage(self.driver)
        checkout_page = CheckoutPage(self.driver)
        checkout_overview_page = CheckoutOverviewPage(self.driver)

        # 1. Открыть сайт магазина
        login_page.open()

        # 2. Авторизоваться как пользователь standard_user
        login_page.login("standard_user", "secret_sauce")

        # Проверяем, что авторизация прошла успешно
        assert inventory_page.get_page_title() == "Products"

        # 3. Добавить товары в корзину
        products_to_add = [
            "Sauce Labs Backpack",
            "Sauce Labs Bolt T-Shirt",
            "Sauce Labs Onesie",
        ]

        for product in products_to_add:
            inventory_page.add_to_cart(product)

        # Проверяем, что в корзине 3 товара
        assert inventory_page.get_cart_count() == 3

        # 4. Перейти в корзину
        inventory_page.go_to_cart()

        # Проверяем, что мы на странице корзины
        assert cart_page.get_page_title() == "Your Cart"

        # Проверяем, что в корзине нужные товары
        cart_items = cart_page.get_cart_item_names()
        for product in products_to_add:
            assert product in cart_items, f"Товар {product} отсутствует в корзине"

        # 5. Нажать кнопку Checkout
        cart_page.click_checkout()

        # Проверяем, что мы на странице оформления заказа
        assert checkout_page.get_page_title() == "Checkout: Your Information"

        # 6. Заполнить форму своими данными
        checkout_page.fill_checkout_form("Иван", "Иванов", "123456")
        checkout_page.click_continue()

        # 7. Проверить итоговую стоимость
        assert checkout_overview_page.get_page_title() == "Checkout: Overview"

        total_text = checkout_overview_page.get_total_text()
        total_value = checkout_overview_page.get_total()

        print(f"Итоговая сумма: {total_text}")

        # 8. Проверка, что итоговая сумма равна $58.29
        assert total_value == 58.29, f"Ожидалось $58.29, но получено ${total_value}"

        # Дополнительные проверки (опционально)
        print(f"Сумма товаров: ${checkout_overview_page.get_item_total()}")
        print(f"Налог: ${checkout_overview_page.get_tax()}")
