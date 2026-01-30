from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("http://uitestingplayground.com/textinput")

    WebDriverWait(driver, 10).until(
        EC.presence_of_element_located((By.ID, "newButtonName"))
    )

    input_field = driver.find_element(By.ID, "newButtonName")
    input_field.clear() 
    input_field.send_keys("SkyPro")
    print("В поле ввода введен текст: SkyPro")
    
    blue_button = driver.find_element(By.ID, "updatingButton")
    blue_button.click()
    print("Нажата синяя кнопка")

    WebDriverWait(driver, 10).until(
        EC.text_to_be_present_in_element((By.ID, "updatingButton"), "SkyPro")
    )
    
    button_text = blue_button.text
    
    print(f"\nТекст кнопки: '{button_text}'")
    

    if button_text == "SkyPro":
        print("✓ Текст кнопки соответствует ожидаемому значению 'SkyPro'")
    else:
        print(f"⚠ Текст кнопки не соответствует ожидаемому. Ожидалось: 'SkyPro', получено: '{button_text}'")
    
finally:

    driver.implicitly_wait(2)
    driver.quit()
    print("\nБраузер закрыт")