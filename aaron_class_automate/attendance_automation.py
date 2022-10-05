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

# Ask Aaron which presentation is it tomorrow
while True:
    aaron_lecture_tomorrow = input("Hello, which lecture is it tomorrow?: ")

    if aaron_lecture_tomorrow == "mmecon":
        presentation_room = config_settings['presentation_mmecon']
        presentation_time = "17:51:00"
        break
    elif aaron_lecture_tomorrow == "denistkachen573":
        presentation_room = config_settings['presentation_denistkachen573']
        presentation_time = "09:00:00"
        break
    else:
        continue

# Check for the time to run the script
now = datetime.now()
current_time = str(now.strftime("%H:%M:%S"))
print("Current Time = ", current_time)

while current_time != presentation_time:
    now = datetime.now()
    current_time = str(now.strftime("%H:%M:%S"))
    print(f"Current time is now: {current_time}, presentation not yet started")

print("Script will now run....")

# Open the web site
driver.get(config_settings['url'])

# Login to the website
login(driver, username, username_nus, password)

# Enter the presentation session
presentation_enter(driver, presentation_room)

driver.quit()


