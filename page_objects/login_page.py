from selenium.webdriver.common.by import By
from locators.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Login:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60, poll_frequency=10)

    def set_username(self, username):
        user = self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.username)))
        user.clear()
        user.send_keys(username)

    def set_password(self, password):
        pwd = self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.password)))
        pwd.clear()
        pwd.send_keys(password)

    def set_submit(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.submit))).click()

    def verify_login(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.user_profile)))


