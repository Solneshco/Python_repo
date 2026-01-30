from selenium.webdriver.common.by import By


class CheckoutPage:
    def __init__(self, driver):
        self.driver = driver
        self.page_title = (By.CSS_SELECTOR, ".title")
        self.first_name_input = (By.ID, "first-name")
        self.last_name_input = (By.ID, "last-name")
        self.postal_code_input = (By.ID, "postal-code")
        self.continue_button = (By.ID, "continue")
        self.cancel_button = (By.ID, "cancel")
        self.error_message = (By.CSS_SELECTOR, ".error-message-container")

    def get_page_title(self):
        return self.driver.find_element(*self.page_title).text

    def enter_first_name(self, first_name):
        self.driver.find_element(*self.first_name_input).send_keys(first_name)
        return self

    def enter_last_name(self, last_name):
        self.driver.find_element(*self.last_name_input).send_keys(last_name)
        return self

    def enter_postal_code(self, postal_code):
        self.driver.find_element(*self.postal_code_input).send_keys(postal_code)
        return self

    def click_continue(self):
        self.driver.find_element(*self.continue_button).click()
        return self

    def click_cancel(self):
        self.driver.find_element(*self.cancel_button).click()
        return self

    def fill_checkout_form(self, first_name, last_name, postal_code):
        self.enter_first_name(first_name)
        self.enter_last_name(last_name)
        self.enter_postal_code(postal_code)
        return self

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
