import pytest
import allure
from selenium import webdriver


@pytest.fixture(scope="function")
def driver(request):
    """
    Фикстура для инициализации WebDriver.
    """
    options = webdriver.ChromeOptions()
    options.add_argument("--headless")  # Для CI/CD
    driver = webdriver.Chrome(options=options)
    
    def teardown():
        """
        Закрытие браузера после теста.
        """
        # Делаем скриншот при падении теста
        if request.node.rep_call.failed:
            allure.attach(
                driver.get_screenshot_as_png(),
                name="screenshot",
                attachment_type=allure.attachment_type.PNG
            )
        driver.quit()
    
    request.addfinalizer(teardown)
    return driver