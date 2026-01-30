from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import pytest


@pytest.fixture
def browser():
    driver = webdriver.Edge()
    driver.maximize_window()
    yield driver
    driver.quit()


def test_01_form(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")

    browser.find_element(By.NAME, "first-name").send_keys("Иван")
    browser.find_element(By.NAME, "last-name").send_keys("Петров")
    browser.find_element(By.NAME, "address").send_keys("Ленина, 55-3")
    browser.find_element(By.NAME, "e-mail").send_keys("test@skypro.com")
    browser.find_element(By.NAME, "phone").send_keys("+7985899998787")
    browser.find_element(By.NAME, "city").send_keys("Москва")
    browser.find_element(By.NAME, "country").send_keys("Россия")
    browser.find_element(By.NAME, "job-position").send_keys("QA")
    browser.find_element(By.NAME, "company").send_keys("SkyPro")

    submit = browser.find_element(By.CSS_SELECTOR, "button[type='submit']")
    browser.execute_script("arguments[0].scrollIntoView();", submit)
    submit.click()

    wait = WebDriverWait(browser, 10)

    # Zip code — красный
    zip_code = wait.until(EC.presence_of_element_located((By.ID, "zip-code")))
    assert "alert-danger" in zip_code.get_attribute("class"), \
        "Поле Zip code должно быть подсвечено красным"

    # Остальные поля — зелёные
    fields_to_check = [
        "first-name",
        "last-name",
        "address",
        "city",
        "country",
        "e-mail",
        "phone",
        "job-position",
        "company"
    ]

    for field_id in fields_to_check:
        field = browser.find_element(By.ID, field_id)
        assert "alert-success" in field.get_attribute("class"), \
            f"Поле {field_id} должно быть подсвечено зелёным"