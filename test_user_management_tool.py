import os

from selenium import webdriver
from page_objects.login_page import Login
from page_objects.admin_page import Admin
from page_objects.pim_page import PIM
from utilities.read_json import read_json

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "data.json")


class Test1:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome()
        cls.driver.maximize_window()
        cls.login = Login(cls.driver)
        cls.admin = Admin(cls.driver)
        cls.pim = PIM(cls.driver)
        cls.config = read_json(CONFIG_FILE)
        cls.user = cls.config["users"][0]

    @classmethod
    def teardown_class(cls):
        cls.driver.close()

    def test_1_login(self):
        self.driver.get(self.config["url"])
        self.login.set_username(self.config["user"])
        self.login.set_password(self.config["password"])
        self.login.set_submit()
        self.login.verify_login()

    def test_2_add_employee(self):
        self.pim.add_emp()

    def test_3_save_employee_details(self):
        firstname, lastname = self.user["name"].split()
        self.pim.set_firstname(firstname)
        self.pim.set_lastname(lastname)
        self.pim.set_emp_id(self.user["emp_id"])
        self.pim.save_emp()

    def test_4_add_user(self):
        self.admin.click_admin()
        self.admin.save_user(self.user["name"], self.user["user_name"], self.user["password"])

    def test_5_find_user(self):
        assert self.admin.find_user(self.user["name"].split()[0]) == self.user["name"]

    def test_6_logout_user(self):
        self.admin.logout_user()

    def test_7_relogin_with_user(self):
        self.login.set_username(self.user["user_name"])
        self.login.set_password(self.user["password"])
        self.login.set_submit()
        self.login.verify_login()