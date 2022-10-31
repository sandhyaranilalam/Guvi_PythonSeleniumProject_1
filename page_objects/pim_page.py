from selenium.webdriver.common.by import By
from locators.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class PIM:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60, poll_frequency=10)

    def click_on_pim(self):
        self.wait.until(ec.presence_of_element_located(((By.XPATH, Locators.pim)))).click()

    def add_employee(self):
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

    def save_employee(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.save_emp))).click()

    def edit_employee(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.edit_employee))).click()

    def update_nickname(self, nickname_to_be_updated):
        nickname = self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.nickname_field)))
        nickname.clear()
        nickname.send_keys(nickname_to_be_updated)

    def delete_employee(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.delete_employee))).click()
