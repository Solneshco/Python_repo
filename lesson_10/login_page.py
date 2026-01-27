import allure
from selenium.webdriver.common.by import By
from .base_page import BasePage


class LoginPage(BasePage):
    """Класс для работы со страницей логина."""
    
    # Локаторы
    USERNAME_INPUT = (By.ID, "username")
    PASSWORD_INPUT = (By.ID, "password")
    LOGIN_BUTTON = (By.ID, "login-button")
    ERROR_MESSAGE = (By.CLASS_NAME, "error-message")
    
    @allure.step("Открыть страницу логина")
    def open(self, url: str) -> None:
        """
        Открыть страницу логина.
        
        Args:
            url: URL страницы логина
        """
        self.driver.get(url)
    
    @allure.step("Авторизоваться с логином '{username}' и паролем '{password}'")
    def login(self, username: str, password: str) -> None:
        """
        Выполнить авторизацию.
        
        Args:
            username: Имя пользователя
            password: Пароль
        """
        self.send_keys(self.USERNAME_INPUT, username)
        self.send_keys(self.PASSWORD_INPUT, password)
        self.click(self.LOGIN_BUTTON)
    
    @allure.step("Получить текст ошибки")
    def get_error_message(self) -> str:
        """
        Получить текст сообщения об ошибке.
        
        Returns:
            str: Текст ошибки
        """
        element = self.find_element(self.ERROR_MESSAGE)
        return element.text