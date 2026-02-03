from selenium.webdriver.common.by import By
import allure


class CartPage:
    """Класс для работы со страницей корзины."""

    def __init__(self, driver):
        """
        Инициализация страницы корзины.

        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.page_title = (By.CSS_SELECTOR, ".title")
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.cart_items = (By.CSS_SELECTOR, ".cart_item")
        self.cart_item_name = (By.CSS_SELECTOR, ".inventory_item_name")
        self.cart_item_price = (By.CSS_SELECTOR, ".inventory_item_price")

    @allure.step("Получить заголовок страницы")
    def get_page_title(self) -> str:
        """
        Получает заголовок страницы.

        Returns:
            str: Текст заголовка страницы
        """
        return self.driver.find_element(*self.page_title).text

    @allure.step("Получить количество товаров в корзине")
    def get_cart_items_count(self) -> int:
        """
        Получает количество товаров в корзине.

        Returns:
            int: Количество товаров в корзине
        """
        return len(self.driver.find_elements(*self.cart_items))

    @allure.step("Получить названия товаров в корзине")
    def get_cart_item_names(self) -> list[str]:
        """
        Получает список названий товаров в корзине.

        Returns:
            list[str]: Список названий товаров
        """
        items = self.driver.find_elements(*self.cart_item_name)
        return [item.text for item in items]

    @allure.step("Получить цены товаров в корзине")
    def get_cart_item_prices(self) -> list[float]:
        """
        Получает список цен товаров в корзине.

        Returns:
            list[float]: Список цен товаров (без символа $)
        """
        items = self.driver.find_elements(*self.cart_item_price)
        return [float(item.text.replace("$", "")) for item in items]

    @allure.step("Удалить товар '{product_name}' из корзины")
    def remove_item(self, product_name: str) -> "CartPage":
        """
        Удаляет товар из корзины.

        Args:
            product_name (str): Название товара для удаления

        Returns:
            CartPage: Экземпляр текущей страницы
        """
        remove_button_locator = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='cart_item']"
            "//button[contains(text(), 'Remove')]",
        )
        self.driver.find_element(*remove_button_locator).click()
        return self

    @allure.step("Нажать кнопку Checkout")
    def click_checkout(self) -> "CartPage":
        """
        Нажимает кнопку оформления заказа.

        Returns:
            CartPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.checkout_button).click()
        return self

    @allure.step("Нажать кнопку Continue Shopping")
    def click_continue_shopping(self) -> "CartPage":
        """
        Нажимает кнопку продолжения покупок.

        Returns:
            CartPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.continue_shopping_button).click()
        return self