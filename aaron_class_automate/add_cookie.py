import json
from selenium import webdriver
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.alert import Alert
import time
from login_info import Aaron
import json
from login import login

def add_the_cookies(driver):

    driver.add_cookie({
        "name": "singularity_visit", 
        "value": "cfa24fba-56fd-4928-8285-8dd05c5ff1b8",
        "path": "/",
        "domain":".pollev.com",
        "secure": "",
        "httpOnly": "",
        "expiry": "2022-10-04T12:50:07.000Z",
        "sameSite": "",
    })

    driver.add_cookie({
        "name": "accept_cookies", 
        "value": "1",
        "path": "/",
        "domain":".pollev.com",
        "secure": "",
        "httpOnly": "",
        "expiry": "2023-10-04T11:50:07.000Z",
        "sameSite": "",
    })

    driver.add_cookie({
        "name": "singularity_visitor", 
        "value": "60395868-7405-4bf0-9dfd-1c76ad0c3239",
        "path": "/",
        "domain":".pollev.com",
        "secure": "",
        "httpOnly": "",
        "expiry": "2023-10-04T11:50:07.000Z",
        "sameSite": "",
    })

    driver.add_cookie({
        "name": "singularity_visit", 
        "value": "cfa24fba-56fd-4928-8285-8dd05c5ff1b8",
        "path": "/",
        "domain":".pollev.com",
        "secure": "",
        "httpOnly": "",
        "expiry": "2022-10-04T12:50:07.000Z",
        "sameSite": "",
    })

    driver.add_cookie({
        "name": "singularity_visit", 
        "value": "cfa24fba-56fd-4928-8285-8dd05c5ff1b8",
        "path": "/",
        "domain":".pollev.com",
        "secure": "",
        "httpOnly": "",
        "expiry": "2022-10-04T12:50:07.000Z",
        "sameSite": "",
    })


