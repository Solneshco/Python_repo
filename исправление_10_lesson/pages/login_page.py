from selenium.webdriver.common.by import By
import allure


class LoginPage:
    """Класс для работы со страницей авторизации."""

    def __init__(self, driver):
        """
        Инициализация страницы авторизации.

        Args:
            driver: WebDriver экземпляр для управления браузером
        """
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, ".error-message-container")

    @allure.step("Открыть страницу авторизации")
    def open(self) -> "LoginPage":
        """
        Открывает страницу авторизации.

        Returns:
            LoginPage: Экземпляр текущей страницы
        """
        self.driver.get("https://www.saucedemo.com/")
        return self

    @allure.step("Ввести имя пользователя: {username}")
    def enter_username(self, username: str) -> "LoginPage":
        """
        Вводит имя пользователя в поле ввода.

        Args:
            username (str): Имя пользователя для ввода

        Returns:
            LoginPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.username_input).send_keys(username)
        return self

    @allure.step("Ввести пароль")
    def enter_password(self, password: str) -> "LoginPage":
        """
        Вводит пароль в поле ввода.

        Args:
            password (str): Пароль для ввода

        Returns:
            LoginPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.password_input).send_keys(password)
        return self

    @allure.step("Нажать кнопку Login")
    def click_login(self) -> "LoginPage":
        """
        Нажимает кнопку входа.

        Returns:
            LoginPage: Экземпляр текущей страницы
        """
        self.driver.find_element(*self.login_button).click()
        return self

    @allure.step("Авторизоваться с именем пользователя: {username}")
    def login(self, username: str, password: str) -> "LoginPage":
        """
        Выполняет полный процесс авторизации.

        Args:
            username (str): Имя пользователя
            password (str): Пароль

        Returns:
            LoginPage: Экземпляр текущей страницы
        """
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    @allure.step("Получить текст сообщения об ошибке")
    def get_error_message(self) -> str:
        """
        Получает текст сообщения об ошибке авторизации.

        Returns:
            str: Текст сообщения об ошибке
        """
        return self.driver.find_element(*self.error_message).text