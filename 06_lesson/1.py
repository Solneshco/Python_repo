from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/ajax")
    
    blue_button = WebDriverWait(driver, 10).until(
        EC.element_to_be_clickable((By.ID, "ajaxButton"))
    )

    blue_button.click()
    print("Нажата синяя кнопка")

    green_banner = WebDriverWait(driver, 15).until(
        EC.visibility_of_element_located((By.ID, "content"))
    )

    WebDriverWait(driver, 15).until(
        lambda d: "Data loaded with AJAX get request." in green_banner.text
    )

    banner_text = green_banner.text.strip()

    print("\nТекст из зеленой плашки:")
    print(banner_text)

    if banner_text == "Data loaded with AJAX get request.":
        print("\n✓ Текст соответствует ожидаемому")
    
finally:

    driver.implicitly_wait(2)
    driver.quit()
    print("\nБраузер закрыт")