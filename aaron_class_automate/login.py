from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time

def login(driver, username, username_nus, password):

    time.sleep(5)
    button_agree_cookie = driver.find_element(By.NAME, "controls").find_element(By.TAG_NAME, "button")
    button_agree_cookie.click()

    some_timeout = 10
    
    # Find the input field at pollev.com

    username_input_field_element_id = "pe-text-field__input-row"
    username_field = WebDriverWait(driver, some_timeout).until(
        EC.element_to_be_clickable((By.CLASS_NAME, username_input_field_element_id)) 
    )

    # Enter the username
    username_field.send_keys(username)

    # Click submit 
    submit_button_class = "component-auth__submit"
    submit_button = driver.find_element(By.CLASS_NAME, submit_button_class)
    submit_button.click()

    time.sleep(5)

    # Re-direct to NUS
    log_in_with_NUS_class = "pe-button__button"
    log_in_with_NUS = driver.find_elements(By.CLASS_NAME, log_in_with_NUS_class)
    log_in_with_NUS[0].click()

    # Enter username and password in NUS
    log_in_to_NUS_username_id = "userNameInput"
    log_in_to_NUS_username = driver.find_element(By.ID, log_in_to_NUS_username_id)
    log_in_to_NUS_username.send_keys(username_nus)

    time.sleep(1)

    log_in_to_NUS_password_id = "passwordInput"
    log_in_to_NUS_password = driver.find_element(By.ID, log_in_to_NUS_password_id)
    log_in_to_NUS_password.send_keys(password)

    time.sleep(1)

    sign_in_nus_id = "submitButton"
    sign_in_nus = driver.find_element(By.ID, sign_in_nus_id)
    sign_in_nus.click()
    
    time.sleep(5)
    return

