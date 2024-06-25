
from selenium import webdriver
import unittest
from Guvi_CapstoneProject1.Source.Functions import TestMethods as tm
from Guvi_CapstoneProject1.Source import locators as lc
from Guvi_CapstoneProject1.Source.locators import LoginLocators as vl


class LoginPageTest(unittest.TestCase):

    def setUp(self):
        self.driver = webdriver.Chrome()
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


    def test_TC_login_01(self):
        self.driver.get(lc.login_url)
        result = tm.login_to_OragneHRM(self.driver,vl.valid_username,vl.valid_password)
        self.assertEqual(result,"The user has logged in successfully")


    def test_TC_login_02(self):
        self.driver.get(lc.login_url)
        result = tm.login_to_OragneHRM(self.driver, vl.valid_username, vl.invalid_password)
        self.assertEqual(result, "Invalid credentials")


    def test_TC_PIM_01(self):
        self.driver.get(lc.login_url)
        tm.login_to_OragneHRM_stat(self.driver,vl.valid_username,vl.valid_password)
        name = tm.random_name()
        result = tm.add_new_employee(self.driver,name[0],name[1])
        self.assertEqual(result,"Successfully Saved")


    def test_TC_PIM_02(self):
        self.driver.get(lc.login_url)
        tm.login_to_OragneHRM_stat(self.driver, vl.valid_username, vl.valid_password)
        result = tm.delete_employee(self.driver)
        self.assertEqual(result,"Successfully Deleted")


    def test_TC_PIM_03(self):
        self.driver.get(lc.login_url)
        tm.login_to_OragneHRM_stat(self.driver, vl.valid_username, vl.valid_password)
        result = tm.edit_employee_details(self.driver)
        self.assertEqual(result,"Successfully Updated")


if __name__ == "__main__":
    unittest.main()