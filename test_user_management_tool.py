import os

from selenium import webdriver
from PageObjects.LoginPage import LoginPage
from utilities.read_json import read_json

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "data.json")


class Test1:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.l1 = LoginPage(cls.driver)
        cls.config = read_json(CONFIG_FILE)
        cls.user = cls.config["users"][0]

    @classmethod
    def teardown_class(cls):
        cls.driver.close()

    def test_1_login(self):
        self.driver.get(self.config["url"])
        self.l1.set_username(self.config["user"])
        self.l1.set_password(self.config["password"])
        self.l1.set_submit()
        self.l1.verify_login()

    def test_2_add_employee(self):
        self.l1.add_emp()

    def test_3_save_employee_details(self):
        firstname, lastname = self.user["name"].split()
        self.l1.set_firstname(firstname)
        self.l1.set_lastname(lastname)
        self.l1.set_emp_id(self.user["emp_id"])
        self.l1.save_emp()

    def test_4_add_user(self):
        self.l1.click_admin()
        self.l1.save_user(self.user["name"], self.user["user_name"], self.user["password"])

    def test_5_find_user(self):
        assert self.l1.find_user(self.user["name"].split()[0]) == self.user["name"]

    def test_6_logout_user(self):
        self.l1.logout_user()

    def test_7_relogin_with_user(self):
        self.l1.set_username(self.user["user_name"])
        self.l1.set_password(self.user["password"])
        self.l1.set_submit()
        self.l1.verify_login()