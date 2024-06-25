
from faker import Faker
from selenium.webdriver.common.by import By
from selenium.webdriver.support.wait import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException
import Guvi_CapstoneProject1.Source.Locators


class TestMethods:

    @staticmethod
    def random_name():
        fake = Faker()
        f_n = fake.first_name()
        l_n = fake.last_name()
        return f_n,l_n


    @staticmethod
    def login_to_OragneHRM(driver,username,password):
        username_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.username_element)))
        password_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.password_element)))
        submit_button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.submit_element)))
        username_element.send_keys(username)
        password_element.send_keys(password)
        submit_button_element.click()
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("dashboard"))
            profile_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, lc.profile_button_element)))
            profile_button.click()
            logout_button = WebDriverWait(driver, 10).until(
                EC.presence_of_element_located((By.XPATH, lc.logout_button_element)))
            logout_button.click()
            result = "The user has logged in successfully"
            return result
        except TimeoutException:
            result = "Invalid credentials"
            return result

    @staticmethod
    def add_new_employee(driver,first,last):
        pim_module = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.pim)))
        pim_module.click()
        add_employee = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.add_employee)))
        add_employee.click()
        first_name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.fir_nam)))
        last_name = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.las_nam)))
        first_name.send_keys(first)
        last_name.send_keys(last)
        save_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.save)))
        save_button.click()
        try:
            toaster = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,lc.saved_success)))
            value = toaster.text
            return value
        except TimeoutException:
            value = "Unable to save"
            return value

    @staticmethod
    def delete_employee(driver):
        pim_module = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.pim)))
        pim_module.click()
        employee_list = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.employee_list)))
        employee_list.click()
        select_user_del = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.sel_user_del)))
        select_user_del.click()
        delete_user = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.delete_user)))
        delete_user.click()
        confirm_delete = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.confirm_del)))
        confirm_delete.click()
        try:
            toaster = WebDriverWait(driver,15).until(EC.presence_of_element_located((By.XPATH,lc.del_success)))
            value = toaster.text
            return value
        except TimeoutException:
            value = "Unable to delete the selected user"
            return value


    @staticmethod
    def edit_employee_details(driver):
        pim_module = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.pim)))
        pim_module.click()
        employee_list = WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, lc.employee_list)))
        employee_list.click()
        select_user = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,)))
        select_user.click()
        edit_user = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.sel_user_edit)))
        edit_user.click()
        male_button = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.male_button)))
        male_button.click()
        submit_edited_user = WebDriverWait(driver,10).until(EC.presence_of_element_located((By.XPATH,lc.submit_edit_user)))
        submit_edited_user.click()
        try:
            toaster = WebDriverWait(driver, 15).until(EC.presence_of_element_located((By.XPATH,lc.update_success)))
            value = toaster.text
            return value
        except TimeoutException:
            value = "Unable to update user details"
            return value

    @staticmethod
    def login_to_OragneHRM_stat(driver, username, password):
        username_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.username_element)))
        password_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.password_element)))
        submit_button_element = WebDriverWait(driver, 10).until(
            EC.presence_of_element_located((By.XPATH, lc.submit_element)))
        username_element.send_keys(username)
        password_element.send_keys(password)
        submit_button_element.click()
        try:
            WebDriverWait(driver, 10).until(
                EC.url_contains("dashboard"))
            result = "The user has logged in successfully"
            return result
        except TimeoutException:
            result = "Invalid credentials"
            return result