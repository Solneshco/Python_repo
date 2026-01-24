from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:
    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    print("Открыта страница с картинками")
    print("Ожидаем загрузки всех картинок...")
    
    images = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    WebDriverWait(driver, 20).until(
        lambda d: all(img.get_attribute("src") for img in d.find_elements(By.TAG_NAME, "img"))
    )
    
    print(f"Найдено картинок: {len(images)}")
    
    if len(images) >= 3:
        third_image = images[2]

        src_value = third_image.get_attribute("src")

        print("\n" + "="*60)
        print("Значение атрибута src у 3-й картинки:")
        print("-"*60)
        print(src_value)
        print("="*60)

        print(f"\nДополнительная информация о 3-й картинке:")
        print(f"ID: {third_image.get_attribute('id')}")
        print(f"Alt текст: {third_image.get_attribute('alt')}")

        if src_value:
            print("✓ Атрибут src содержит значение")
        else:
            print("⚠ Атрибут src пустой!")
    else:
        print(f"⚠ На странице меньше 3 картинок! Найдено только: {len(images)}")
    
finally:
    driver.implicitly_wait(2)
    driver.quit()
    print("\nБраузер закрыт")
    from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

driver = webdriver.Chrome()

try:

    driver.get("https://bonigarcia.dev/selenium-webdriver-java/loading-images.html")
    
    print("Открыта страница с картинками")
    print("Ожидаем загрузки всех картинок...")

    images = WebDriverWait(driver, 20).until(
        EC.presence_of_all_elements_located((By.TAG_NAME, "img"))
    )

    WebDriverWait(driver, 20).until(
        lambda d: all(img.get_attribute("src") for img in d.find_elements(By.TAG_NAME, "img"))
    )
    
    print(f"Найдено картинок: {len(images)}")
    
    if len(images) >= 3:
        third_image = images[2]
        
        src_value = third_image.get_attribute("src")
        
        print("\n" + "="*60)
        print("Значение атрибута src у 3-й картинки:")
        print("-"*60)
        print(src_value)
        print("="*60)
        
        print(f"\nДополнительная информация о 3-й картинке:")
        print(f"ID: {third_image.get_attribute('id')}")
        print(f"Alt текст: {third_image.get_attribute('alt')}")
        
        if src_value:
            print("✓ Атрибут src содержит значение")
        else:
            print("⚠ Атрибут src пустой!")
    else:
        print(f"⚠ На странице меньше 3 картинок! Найдено только: {len(images)}")
    
finally:
    driver.implicitly_wait(2)
    driver.quit()
    print("\nБраузер закрыт")