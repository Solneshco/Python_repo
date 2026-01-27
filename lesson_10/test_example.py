import pytest
import allure
from pages.login_page import LoginPage


@allure.feature("Авторизация")
@allure.severity(allure.severity_level.CRITICAL)
class TestLogin:
    
    @allure.title("Успешная авторизация")
    @allure.description("Проверка успешной авторизации с валидными данными")
    def test_successful_login(self, driver):
        """
        Тест успешной авторизации.
        """
        login_page = LoginPage(driver)
        
        with allure.step("Открыть страницу логина"):
            login_page.open("https://example.com/login")
        
        with allure.step("Выполнить авторизацию"):
            login_page.login("test_user", "test_password")
        
        with allure.step("Проверить редирект на главную страницу"):
            assert "dashboard" in driver.current_url
    
    @allure.title("Неуспешная авторизация с неверным паролем")
    @allure.description("Проверка отображения ошибки при неверном пароле")
    def test_failed_login(self, driver):
        """
        Тест неуспешной авторизации.
        """
        login_page = LoginPage(driver)
        
        with allure.step("Открыть страницу логина"):
            login_page.open("https://example.com/login")
        
        with allure.step("Выполнить авторизацию с неверными данными"):
            login_page.login("test_user", "wrong_password")
        
        with allure.step("Проверить сообщение об ошибке"):
            error_text = login_page.get_error_message()
            assert "неверный пароль" in error_text.lower()