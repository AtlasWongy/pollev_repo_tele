from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
import time
from selenium.common.exceptions import NoSuchElementException
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from telegram_bot_send.send_reminder import send_the_reminder
import linecache

def presentation_enter(driver, room):

    some_timeout = 7

    # Enter the room through the text input
    input_field_text_class = "pe-text-field__input"
    input_field_text = WebDriverWait(driver, some_timeout).until(
        EC.element_to_be_clickable((By.CLASS_NAME, input_field_text_class))
    )
    input_field_text.send_keys(room)

    # Click the join button
    submit_button_class = "pollev-home-join__submit"
    submit_button = WebDriverWait(driver, some_timeout).until(
        EC.element_to_be_clickable((By.CLASS_NAME, submit_button_class))
    )
    submit_button.click()

    time.sleep(5)

    waiting_presentation_start_banner_class = "pec-response-hold__header"
    # Try to find the element -> presentation not started
    # Refresh page every 30 seconds
    # When element cannot be found, send the telegram notification
    loop_again = True
    
    while loop_again:
        try:
            time.sleep(3)
            WebDriverWait(driver, some_timeout).until(
                EC.element_to_be_clickable((By.CLASS_NAME, waiting_presentation_start_banner_class))
            ) 
            driver.refresh()
        except TimeoutException:

            # Check if the last poll's questions matches this poll's question
            # Use line cache
            # if it matches, then continue the while loop of refreshing

            check_last_poll_questions = linecache.getlines("constants.txt", -1)
            print(f"The last poll question is {check_last_poll_questions[-1]}")

            question_class_name = "component-response-header__title"
            get_the_question_web_element = WebDriverWait(driver, some_timeout).until(
                EC.element_to_be_clickable((By.CLASS_NAME, question_class_name))
            )
            get_the_question_text = get_the_question_web_element.text
            
            if check_last_poll_questions[-1].strip() == get_the_question_text:
                print("No new updated questions")
                driver.refresh()
                continue

            # Send telegram notification
            send_the_reminder()
            print("Send Aaron!!")
            loop_again = False
        
    # Let aaron fill in his answers
    doing_the_poll_loop = True

    while doing_the_poll_loop:

        checks_input = input("Waiting for aaron input: ")

        if checks_input == "aarondone":
            print("Grab last question")

            # Save the Poll question into a Text File
            question_title_class_name = "component-response-header__title"
            save_the_last_question_web_element = WebDriverWait(driver, some_timeout).until(
                EC.element_to_be_clickable((By.CLASS_NAME, question_title_class_name))
            )
            save_the_last_question_text = save_the_last_question_web_element.text

            with open("constants.txt", "w") as text_file:
                text_file.write(save_the_last_question_text)

            print("End the script")

            return 
        else:
            continue

    # send_the_reminder()
    return


