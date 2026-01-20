from selenium.webdriver.common.by import By

class MainPage:
    def __init__(self, driver):
        self.driver = driver
        self.item_map = {
            "Sauce Labs Backpack": "add-to-cart-sauce-labs-backpack",
            "Sauce Labs Bolt T-Shirt": "add-to-cart-sauce-labs-bolt-t-shirt",
            "Sauce Labs Onesie": "add-to-cart-sauce-labs-onesie"
        }
    
    def add_item_to_cart(self, item_name):
        button_id = self.item_map.get(item_name)
        if button_id:
            self.driver.find_element(By.ID, button_id).click()
        return self
    
    def go_to_cart(self):
        self.driver.find_element(By.CLASS_NAME, "shopping_cart_link").click()
        from pages.cart_page import CartPage
        return CartPage(self.driver)