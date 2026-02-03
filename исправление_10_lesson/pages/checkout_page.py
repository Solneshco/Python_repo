from selenium.webdriver.common.by import By
import allure


class CheckoutPage:
    """Класс для работы со страницей оформления заказа."""

    def __init__(self, driver):
        """
        Инициализация страницы оформления заказа.

        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.page_title = (By.CSS_SELECTOR, ".title")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.cancel_button = (By.ID, "cancel")
        self.error_message = (By.CSS_SELECTOR, ".error-message-container")

    @allure.step("Получить заголовок страницы")
    def get_page_title(self) -> str:
        """
        Получает заголовок страницы.

        Returns:
            str: Текст заголовка страницы
        """
        return self.driver.find_element(*self.page_title).text

    @allure.step("Ввести имя: {first_name}")
    def enter_first_name(self, first_name: str) -> "CheckoutPage":
        """
        Вводит имя в поле ввода.

        Args:
            first_name (str): Имя для ввода

        Returns:
            CheckoutPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        return self

    @allure.step("Ввести фамилию: {last_name}")
    def enter_last_name(self, last_name: str) -> "CheckoutPage":
        """
        Вводит фамилию в поле ввода.

        Args:
            last_name (str): Фамилия для ввода

        Returns:
            CheckoutPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        return self

    @allure.step("Ввести почтовый индекс: {postal_code}")
    def enter_postal_code(self, postal_code: str) -> "CheckoutPage":
        """
        Вводит почтовый индекс в поле ввода.

        Args:
            postal_code (str): Почтовый индекс для ввода

        Returns:
            CheckoutPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        return self

    @allure.step("Нажать кнопку Continue")
    def click_continue(self) -> "CheckoutPage":
        """
        Нажимает кнопку продолжения оформления заказа.

        Returns:
            CheckoutPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.continue_button).click()
        return self

    @allure.step("Нажать кнопку Cancel")
    def click_cancel(self) -> "CheckoutPage":
        """
        Нажимает кнопку отмены оформления заказа.

        Returns:
            CheckoutPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.cancel_button).click()
        return self

    @allure.step("Заполнить форму оформления заказа")
    def fill_checkout_form(self, first_name: str, last_name: str, postal_code: str) -> "CheckoutPage":
        """
        Заполняет все поля формы оформления заказа.

        Args:
            first_name (str): Имя
            last_name (str): Фамилия
            postal_code (str): Почтовый индекс

        Returns:
            CheckoutPage: Экземпляр текущей страницы
        """
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        return self

    @allure.step("Получить текст сообщения об ошибке")
    def get_error_message(self) -> str:
        """
        Получает текст сообщения об ошибке.

        Returns:
            str: Текст сообщения об ошибке
        """
        return self.driver.find_element(*self.error_message).text