from selenium.webdriver.common.by import By
from locators.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PIM:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60, poll_frequency=10)

    def add_emp(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.add))).click()

    def set_firstname(self, fname):
        user = self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.firstName)))
        user.send_keys(fname)

    def set_lastname(self, lname):
        user = self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.lastname)))
        user.send_keys(lname)

    def set_emp_id(self, id):
        user = self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.emp_id)))
        user.clear()
        user.send_keys(id)

    def save_emp(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.save_emp))).click()
