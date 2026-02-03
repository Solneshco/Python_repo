import allure
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class BasePage:
    """Базовый класс для всех страниц."""
    
    def __init__(self, driver: 'webdriver', timeout: int = 10) -> None:
        """
        Инициализация базовой страницы.
        
        Args:
            driver: WebDriver экземпляр
            timeout: Время ожидания элементов (по умолчанию 10 секунд)
        """
        self.driver = driver
        self.wait = WebDriverWait(driver, timeout)
    
    @allure.step("Поиск элемента: {locator}")
    def find_element(self, locator: tuple, timeout: int = None) -> 'WebElement':
        """
        Поиск элемента на странице с ожиданием.
        
        Args:
            locator: Кортеж (By, значение)
            timeout: Время ожидания (опционально)
            
        Returns:
            WebElement: Найденный элемент
            
        Raises:
            TimeoutException: Если элемент не найден за время ожидания
        """
        wait = self.wait if timeout is None else WebDriverWait(self.driver, timeout)
        return wait.until(EC.presence_of_element_located(locator))
    
    @allure.step("Клик по элементу: {locator}")
    def click(self, locator: tuple) -> None:
        """
        Клик по элементу.
        
        Args:
            locator: Кортеж (By, значение)
        """
        element = self.find_element(locator)
        element.click()
    
    @allure.step("Ввод текста '{text}' в элемент: {locator}")
    def send_keys(self, locator: tuple, text: str) -> None:
        """
        Ввод текста в элемент.
        
        Args:
            locator: Кортеж (By, значение)
            text: Текст для ввода
        """
        element = self.find_element(locator)
        element.clear()
        element.send_keys(text)