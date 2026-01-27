from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver

    def verify_item_in_cart(self, item_name):
        # Вспомогательный метод для отладки (без assert в классе страницы)
        items = self.driver.find_elements(By.CLASS_NAME, "inventory_item_name")
        item_names = [item.text for item in items]
        return item_name in item_names

    def click_checkout(self):
        self.driver.find_element(By.ID, "checkout").click()
        from .checkout_page import CheckoutStepOnePage
        return CheckoutStepOnePage(self.driver)