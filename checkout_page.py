from selenium.webdriver.common.by import By

class CheckoutStepOnePage:
    def __init__(self, driver):
        self.driver = driver
    
    def fill_shipping_info(self, first_name, last_name, postal_code):
        self.driver.find_element(By.ID, "first-name").send_keys(first_name)
        self.driver.find_element(By.ID, "last-name").send_keys(last_name)
        self.driver.find_element(By.ID, "postal-code").send_keys(postal_code)
        return self
    
    def click_continue(self):
        self.driver.find_element(By.ID, "continue").click()
        return CheckoutStepTwoPage(self.driver)

class CheckoutStepTwoPage:
    def __init__(self, driver):
        self.driver = driver
    
    def get_total_price(self):
        # Метод возвращает текст элемента с итоговой суммой
        total_element = self.driver.find_element(By.CLASS_NAME, "summary_total_label")
        return total_element.text