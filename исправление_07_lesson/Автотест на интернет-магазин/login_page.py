from selenium.webdriver.common.by import By


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.username_input = (By.ID, "user-name")
        self.password_input = (By.ID, "password")
        self.login_button = (By.ID, "login-button")
        self.error_message = (By.CSS_SELECTOR, ".error-message-container")

    def open(self):
        self.driver.get("https://www.saucedemo.com/")
        return self

    def enter_username(self, username):
        self.driver.find_element(*self.username_input).send_keys(username)
        return self

    def enter_password(self, password):
        self.driver.find_element(*self.password_input).send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(*self.login_button).click()
        return self

    def login(self, username, password):
        self.enter_username(username)
        self.enter_password(password)
        self.click_login()
        return self

    def get_error_message(self):
        return self.driver.find_element(*self.error_message).text
