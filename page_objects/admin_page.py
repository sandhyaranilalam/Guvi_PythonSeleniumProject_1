import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from locators.locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class Admin:
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 60, poll_frequency=10)

    def click_admin(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.admin))).click()

    def save_user(self, emp_name, username, password):
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.add_user_click))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.user_role))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.user_role_value))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.emp_name))).send_keys(emp_name.split()[0])
        time.sleep(5)
        auto_suggest = self.driver.find_elements(By.XPATH, Locators.auto_suggest_emp_value)
        act = ActionChains(self.driver)
        for ele in auto_suggest:
            if ele.text == emp_name:
                act.move_to_element(ele).click().perform()
                break
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.status_click))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.status_dropdown_value))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.emp_username))).send_keys(username)
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.emp_password))).send_keys(password)
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.emp_cpassword))).send_keys(password)
        time.sleep(5)
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.save_user))).click()

    def find_user(self, user):
        return self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.added_user.format(user)))).text

    def logout_user(self):
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.profile))).click()
        self.wait.until(ec.presence_of_element_located((By.XPATH, Locators.logout))).click()
