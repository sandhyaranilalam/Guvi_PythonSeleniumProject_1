import os

from selenium import webdriver
from page_objects.login_page import Login
from page_objects.admin_page import Admin
from page_objects.pim_page import PIM
from utilities.read_json import read_json
from webdriver_manager.chrome import ChromeDriverManager

CONFIG_FILE = os.path.join(os.path.dirname(os.path.abspath(__file__)), "config", "data.json")


class Test1:
    @classmethod
    def setup_class(cls):
        cls.driver = webdriver.Chrome(ChromeDriverManager().install())
        cls.driver.maximize_window()
        cls.login = Login(cls.driver)
        cls.admin = Admin(cls.driver)
        cls.pim = PIM(cls.driver)
        cls.config = read_json(CONFIG_FILE)
        cls.valid_user = cls.config["users"][0]

    @classmethod
    def teardown_class(cls):
        cls.driver.close()

    def test_1_invalid_login(self):
        self.driver.get(self.config["url"])
        self.login.set_username(str(self.config["user"]).upper())
        self.login.set_password(str(self.config["password"]).upper())
        self.login.set_submit()
        self.login.check_invalid_credentials_alert()

    def test_2_valid_login(self):
        self.driver.get(self.config["url"])
        self.login.set_username(self.config["user"])
        self.login.set_password(self.config["password"])
        self.login.set_submit()
        self.login.verify_login()

    def test_3_add_new_employee(self):
        self.pim.click_on_pim()
        self.pim.add_employee()
        firstname, lastname = self.valid_user["name"].split()
        self.pim.set_firstname(firstname)
        self.pim.set_lastname(lastname)
        self.pim.set_emp_id(self.valid_user["emp_id"])
        self.pim.save_employee()

    def test_4_edit_existing_employee(self):
        self.pim.click_on_pim()
        self.pim.edit_employee()
        firstname, lastname = self.valid_user["name"].split()
        self.pim.update_nickname(firstname.upper())
        self.pim.save_employee()

    def test_5_delete_existing_employee(self):
        self.pim.click_on_pim()
        self.pim.delete_employee()
    """
    def test_5_add_user(self):
        self.admin.click_admin()
        self.admin.save_user(self.valid_user["name"], self.valid_user["user_name"], self.valid_user["password"])

    def test_6_find_user(self):
        assert self.admin.find_user(self.valid_user["name"].split()[0]) == self.valid_user["name"]

    def test_7_logout_user(self):
        self.admin.logout_user()

    def test_8_relogin_with_user(self):
        self.login.set_username(self.valid_user["user_name"])
        self.login.set_password(self.valid_user["password"])
        self.login.set_submit()
        self.login.verify_login()
    """