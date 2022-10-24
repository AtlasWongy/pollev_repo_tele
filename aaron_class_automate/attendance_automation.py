import json
from selenium import webdriver
from login_info import Aaron
import json
from login import login
from enter_presentation_room import presentation_enter
from datetime import datetime

open_config = open("config.json")
config_settings = json.load(open_config)

path = config_settings['driver_path']
driver = webdriver.Chrome(executable_path=path)

aaron_instance = Aaron()
username = aaron_instance.username
username_nus = aaron_instance.username_nus
password = aaron_instance.password

# Ask Aaron which class is it
while True:
    current_class = input("Which class is it today? ")

    if current_class == "mmecon":
        presentation_room = config_settings['class_mmecon']
        break
    elif current_class == "denist":
        presentation_room = config_settings['class_denistkachen573']
        break
    elif current_class == "testing":
        presentation_room = config_settings['class_testing']
        break
    else:
        print("It seems the class you are attending is not known..")
        print("Please try again")
        continue

print("Script will now run....")

# Open the web site
driver.get(config_settings['url'])

# Login to the website
login(driver, username, username_nus, password)

# Ensure the constant.txt file is not empty
with open("constants.txt", "r") as text_file:
    if text_file.readline() == "":
        with open("constants.txt", "w") as file_write:
            file_write.write("PlaceHolder")

# Enter the presentation session
presentation_enter(driver, presentation_room)

driver.quit()


