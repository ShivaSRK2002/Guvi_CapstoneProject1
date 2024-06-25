


# file_path = "/Users/dilipkumar.g/PycharmProjects/pythonProject1/DataDrivenFramework/Data/login_creds.xls"
login_url = "https://opensource-demo.orangehrmlive.com/web/index.php/auth/login"
home_url = "https://opensource-demo.orangehrmlive.com/web/index.php/dashboard/index"



class LoginLocators:
    username_element = "//input[@name='username']"
    password_element = "//input[@name='password']"
    submit_element = "//button[@type='submit']"
    profile_button_element = "//span[@class='oxd-userdropdown-tab']"
    logout_button_element = "//a[text()='Logout']"
    valid_username = "Admin"
    valid_password = "admin123"
    invalid_username = "admin"
    invalid_password = "boom"
    add_employee = "//a[text()='Add Employee']"
    pim = "//span[text()='PIM']"
    fir_nam = "//input[@name='firstName']"
    las_nam = "//input[@name='lastName']"
    save = "//button[text()=' Save ']"
    saved_success = "//p[text()='Successfully Saved']"
    employee_list = "//a[text()='Employee List']"
    sel_user_del = "((//div[@role='row'])[3]//child::div)[1]"
    delete_user = "//button[text()=' Delete Selected ']"
    confirm_del = "//button[text()=' Yes, Delete ']"
    del_success = "//p[text()='Successfully Deleted']"
    sel_user_edit = "((//div[@role='row'])[3]//child::div)[1]"
    male_button = "//label[text()='Male']"
    submit_edit_user = "(//button[@type='submit'])[1]"
    update_success = "//p[text()='Successfully Updated']"