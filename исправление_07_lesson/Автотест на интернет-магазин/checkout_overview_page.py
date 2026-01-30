from selenium.webdriver.common.by import By


class CheckoutOverviewPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.CSS_SELECTOR, ".title")
        self.finish_button = (By.ID, "finish")
        self.cancel_button = (By.ID, "cancel")
        self.item_total = (By.CSS_SELECTOR, ".summary_subtotal_label")
        self.tax = (By.CSS_SELECTOR, ".summary_tax_label")
        self.total = (By.CSS_SELECTOR, ".summary_total_label")
        self.items_list = (By.CSS_SELECTOR, ".cart_item")

    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text

    def get_item_total(self):
        text = self.driver.find_element(*self.item_total).text
        return float(text.replace("Item total: $", ""))

    def get_tax(self):
        text = self.driver.find_element(*self.tax).text
        return float(text.replace("Tax: $", ""))

    def get_total(self):
        text = self.driver.find_element(*self.total).text
        return float(text.replace("Total: $", ""))

    def get_total_text(self):
        return self.driver.find_element(*self.total).text

    def click_finish(self):
        self.driver.find_element(*self.finish_button).click()
        return self

    def click_cancel(self):
        self.driver.find_element(*self.cancel_button).click()
        return self

    def get_items_count(self):
        return len(self.driver.find_elements(*self.items_list))
