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


def test_form_validation(browser):
    browser.get("https://bonigarcia.dev/selenium-webdriver-java/data-types.html")
    
    first_name = browser.find_element(By.CSS_SELECTOR, 'input[name="first-name"]')
    first_name.send_keys("Иван")

    last_name = browser.find_element(By.CSS_SELECTOR, 'input[name="last-name"]')
    last_name.send_keys("Петров")

    address = browser.find_element(By.CSS_SELECTOR, 'input[name="address"]')
    address.send_keys("Ленина, 55-3")

    email = browser.find_element(By.CSS_SELECTOR, 'input[name="e-mail"]')
    email.send_keys("test@skypro.com")

    phone = browser.find_element(By.CSS_SELECTOR, 'input[name="phone"]')
    phone.send_keys("+7985899998787")
    

    city = browser.find_element(By.CSS_SELECTOR, 'input[name="city"]')
    city.send_keys("Москва")

    country = browser.find_element(By.CSS_SELECTOR, 'input[name="country"]')
    country.send_keys("Россия")

    job_position = browser.find_element(By.CSS_SELECTOR, 'input[name="job-position"]')
    job_position.send_keys("QA")

    company = browser.find_element(By.CSS_SELECTOR, 'input[name="company"]')
    company.send_keys("SkyPro")
    
    submit_button = browser.find_element(By.CSS_SELECTOR, 'button[type="submit"]')
    submit_button.click()

    wait = WebDriverWait(browser, 10)

    zip_code_field = wait.until(
        EC.presence_of_element_located((By.CSS_SELECTOR, 'input[name="zip-code"]'))
    )

    zip_code_classes = zip_code_field.get_attribute("class")

    assert "is-invalid" in zip_code_classes, "Поле Zip code должно быть подсвечено красным"

    fields_to_check = [
        'first-name',
        'last-name',
        'address',
        'e-mail',
        'phone',
        'city',
        'country',
        'job-position',
        'company'
    ]
    
    for field_name in fields_to_check:
        field = browser.find_element(By.CSS_SELECTOR, f'input[name="{field_name}"]')
        field_classes = field.get_attribute("class")
        

        assert "is-valid" in field_classes, f"Поле {field_name} должно быть подсвечено зеленым"
    
    print("Все проверки пройдены успешно!")


if __name__ == "__main__":
    pytest.main([__file__, "-v"])