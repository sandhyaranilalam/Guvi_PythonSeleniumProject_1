import time

from selenium.webdriver import ActionChains
from selenium.webdriver.common.by import By
from PageObjects.Locators import Locators
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as ec


class LoginPage:
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

