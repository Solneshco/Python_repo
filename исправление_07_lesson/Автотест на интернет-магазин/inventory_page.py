from selenium.webdriver.common.by import By


class InventoryPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.CSS_SELECTOR, ".title")
        self.shopping_cart = (By.CSS_SELECTOR, ".shopping_cart_link")
        self.menu_button = (By.ID, "react-burger-menu-btn")
        self.logout_link = (By.ID, "logout_sidebar_link")

    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text

    def add_to_cart(self, product_name):
        # Ищем кнопку "Add to cart" для конкретного товара
        add_button_locator = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']"
            "//button[contains(text(), 'Add to cart')]",
        )
        self.driver.find_element(*add_button_locator).click()
        return self

    def remove_from_cart(self, product_name):
        # Ищем кнопку "Remove" для конкретного товара
        remove_button_locator = (
            By.XPATH,
            f"//div[text()='{product_name}']/ancestor::div[@class='inventory_item']"
            "//button[contains(text(), 'Remove')]",
        )
        self.driver.find_element(*remove_button_locator).click()
        return self

    def go_to_cart(self):
        self.driver.find_element(*self.shopping_cart).click()
        return self

    def logout(self):
        self.driver.find_element(*self.menu_button).click()
        from selenium.webdriver.support.ui import WebDriverWait
        from selenium.webdriver.support import expected_conditions as EC

        wait = WebDriverWait(self.driver, 10)
        logout_element = wait.until(EC.element_to_be_clickable(self.logout_link))
        logout_element.click()
        return self

    def get_cart_count(self):
        cart_badge = (By.CSS_SELECTOR, ".shopping_cart_badge")
        elements = self.driver.find_elements(*cart_badge)
        if elements:
            return int(elements[0].text)
        return 0
