from selenium.webdriver.common.by import By
import allure


class CheckoutOverviewPage:
    """Класс для работы со страницей обзора заказа."""

    def __init__(self, driver):
        """
        Инициализация страницы обзора заказа.

        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.page_title = (By.CSS_SELECTOR, ".title")
        self.finish_button = (By.ID, "finish")
        self.cancel_button = (By.ID, "cancel")
        self.item_total = (By.CSS_SELECTOR, ".summary_subtotal_label")
        self.tax = (By.CSS_SELECTOR, ".summary_tax_label")
        self.total = (By.CSS_SELECTOR, ".summary_total_label")
        self.items_list = (By.CSS_SELECTOR, ".cart_item")

    @allure.step("Получить заголовок страницы")
    def get_page_title(self) -> str:
        """
        Получает заголовок страницы.

        Returns:
            str: Текст заголовка страницы
        """
        return self.driver.find_element(*self.page_title).text

    @allure.step("Получить сумму товаров")
    def get_item_total(self) -> float:
        """
        Получает общую сумму товаров.

        Returns:
            float: Сумма товаров
        """
        text = self.driver.find_element(*self.item_total).text
        return float(text.replace("Item total: $", ""))

    @allure.step("Получить сумму налога")
    def get_tax(self) -> float:
        """
        Получает сумму налога.

        Returns:
            float: Сумма налога
        """
        text = self.driver.find_element(*self.tax).text
        return float(text.replace("Tax: $", ""))

    @allure.step("Получить итоговую сумму")
    def get_total(self) -> float:
        """
        Получает итоговую сумму заказа.

        Returns:
            float: Итоговая сумма
        """
        text = self.driver.find_element(*self.total).text
        return float(text.replace("Total: $", ""))

    @allure.step("Получить текст итоговой суммы")
    def get_total_text(self) -> str:
        """
        Получает текст итоговой суммы.

        Returns:
            str: Текст итоговой суммы
        """
        return self.driver.find_element(*self.total).text

    @allure.step("Нажать кнопку Finish")
    def click_finish(self) -> "CheckoutOverviewPage":
        """
        Нажимает кнопку завершения заказа.

        Returns:
            CheckoutOverviewPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.finish_button).click()
        return self

    @allure.step("Нажать кнопку Cancel")
    def click_cancel(self) -> "CheckoutOverviewPage":
        """
        Нажимает кнопку отмены заказа.

        Returns:
            CheckoutOverviewPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.cancel_button).click()
        return self

    @allure.step("Получить количество товаров в заказе")
    def get_items_count(self) -> int:
        """
        Получает количество товаров в заказе.

        Returns:
            int: Количество товаров
        """
        return len(self.driver.find_elements(*self.items_list))