class Locators:
    username = "//input[@name='username']"
    password = "//input[@name='password']"
    submit = "//button[text()=' Login ']"
    user_profile = "//*[@class='oxd-userdropdown-img']"
    invalid_credentials_alert = "//*[@id='app']/div[1]/div/div[1]/div/div[2]/div[2]/div/div[1]/div[1]/p"

    pim = "//span[text()='PIM']"
    edit_employee = "//*[@class='oxd-icon-button oxd-table-cell-action-space']/i[@class='oxd-icon bi-pencil-fill']"
    delete_employee = "//*[@class='oxd-icon-button oxd-table-cell-action-space']/i[@class='oxd-icon bi-trash']"
    nickname_field = "//*[text()='Nickname']/ancestor::div[@class='oxd-input-group__label-wrapper']" \
                     "/following-sibling::div/input"

    add = "//button[text()=' Add ']"
    firstName = '//input[@name="firstName"]'
    lastname = '//input[@name="lastName"]'
    emp_id = '//div[@class="oxd-form-row"]/div[2]/div/div/div[2]/input'
    save_emp = "//button[text()=' Save ']"
    admin = "//span[text()='Admin']"
    add_user_click = "//button[text()=' Add ']"
    user_role = '//div[@class="oxd-form-row"]/div/div[1]/div/div[2]/div/div/div[1]'
    user_role_value = "//span[text()='ESS']"
    emp_name = '//div[@class="oxd-form-row"]/div/div[2]/div/div[2]/div/div/input'
    auto_suggest_emp_value = "//div[@role='option']/span"
    status_click = '//div[@class="oxd-form-row"]/div/div[3]/div/div[2]/div/div/div[1]'
    status_dropdown_value = "//span[text()='Enabled']"
    emp_username = '//div[@class="oxd-form-row"]/div/div[4]/div/div[2]/input'
    emp_password = '//form[@class="oxd-form"]/div[2]/div/div/div/div[2]/input'
    emp_cpassword = '//form[@class="oxd-form"]/div[2]/div/div[2]/div/div[2]/input'
    save_user = '//button[@type="submit"]'

    added_user = '//div[contains(text(), "{}")]'
    profile ='//span[@class="oxd-userdropdown-tab"]'
    logout= '//a[text()="Logout"]'
