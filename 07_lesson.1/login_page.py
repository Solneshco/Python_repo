from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC


class LoginPage:
    def __init__(self, driver):
        self.driver = driver
        self.url = "https://www.saucedemo.com/"

    def open(self):
        self.driver.get(self.url)
        return self

    def enter_username(self, username):
        WebDriverWait(self.driver, 10).until(
            EC.visibility_of_element_located((By.ID, "user-name"))
        ).send_keys(username)
        return self

    def enter_password(self, password):
        self.driver.find_element(By.ID, "password").send_keys(password)
        return self

    def click_login(self):
        self.driver.find_element(By.ID, "login-button").click()
        from .main_page import MainPage
        return MainPage(self.driver)