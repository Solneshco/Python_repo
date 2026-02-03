from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import allure


class InventoryPage:
    """Класс для работы со страницей каталога товаров."""

    def __init__(self, driver):
        """
        Инициализация страницы каталога товаров.

        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.page_title = (By.CSS_SELECTOR, ".title")
        self.shopping_cart = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    @allure.step("Получить заголовок страницы")
    def get_page_title(self) -> str:
        """
        Получает заголовок страницы.

        Returns:
            str: Текст заголовка страницы
        """
        return self.driver.find_element(*self.page_title).text

    @allure.step("Добавить товар '{product_name}' в корзину")
    def add_to_cart(self, product_name: str) -> "InventoryPage":
        """
        Добавляет товар в корзину.

        Args:
            product_name (str): Название товара для добавления

        Returns:
            InventoryPage: Экземпляр текущей страницы
        """
        add_button_locator = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']"
            "//button[contains(text(), 'Add to cart')]",
        )
        self.driver.find_element(*add_button_locator).click()
        return self

    @allure.step("Удалить товар '{product_name}' из корзины")
    def remove_from_cart(self, product_name: str) -> "InventoryPage":
        """
        Удаляет товар из корзины.

        Args:
            product_name (str): Название товара для удаления

        Returns:
            InventoryPage: Экземпляр текущей страницы
        """
        remove_button_locator = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']"
            "//button[contains(text(), 'Remove')]",
        )
        self.driver.find_element(*remove_button_locator).click()
        return self

    @allure.step("Перейти в корзину")
    def go_to_cart(self) -> "InventoryPage":
        """
        Переходит на страницу корзины.

        Returns:
            InventoryPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.shopping_cart).click()
        return self

    @allure.step("Выйти из системы")
    def logout(self) -> "InventoryPage":
        """
        Выполняет выход из системы.

        Returns:
            InventoryPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.menu_button).click()
        wait = WebDriverWait(self.driver, 10)
        logout_element = wait.until(EC.element_to_be_clickable(self.logout_link))
        logout_element.click()
        return self

    @allure.step("Получить количество товаров в корзине")
    def get_cart_count(self) -> int:
        """
        Получает количество товаров в корзине.

        Returns:
            int: Количество товаров в корзине (0, если корзина пуста)
        """
        cart_badge = (By.CSS_SELECTOR, ".shopping_cart_badge")
        elements = self.driver.find_elements(*cart_badge)
        if elements:
            return int(elements[0].text)
        return 0