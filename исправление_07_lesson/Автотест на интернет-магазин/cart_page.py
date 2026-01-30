from selenium.webdriver.common.by import By


class CartPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.CSS_SELECTOR, ".title")
        self.checkout_button = (By.ID, "checkout")
        self.continue_shopping_button = (By.ID, "continue-shopping")
        self.cart_items = (By.CSS_SELECTOR, ".cart_item")
        self.cart_item_name = (By.CSS_SELECTOR, ".inventory_item_name")
        self.cart_item_price = (By.CSS_SELECTOR, ".inventory_item_price")

    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text

    def get_cart_items_count(self):
        return len(self.driver.find_elements(*self.cart_items))

    def get_cart_item_names(self):
        items = self.driver.find_elements(*self.cart_item_name)
        return [item.text for item in items]

    def get_cart_item_prices(self):
        items = self.driver.find_elements(*self.cart_item_price)
        return [float(item.text.replace("$", "")) for item in items]

    def remove_item(self, product_name):
        remove_button_locator = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='cart_item']"
            "//button[contains(text(), 'Remove')]",
        )
        self.driver.find_element(*remove_button_locator).click()
        return self

    def click_checkout(self):
        self.driver.find_element(*self.checkout_button).click()
        return self

    def click_continue_shopping(self):
        self.driver.find_element(*self.continue_shopping_button).click()
        return self
