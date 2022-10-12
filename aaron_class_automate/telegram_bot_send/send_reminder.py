import requests

TOKEN = "5663501363:AAEQtcQd2AM-vuVecfd1doHFDLLNl_hbOyM"
yijie_chat_id = "127764571"
aaron_chat_id = "101064221"
group_chat_reminder = "-837370543"

def send_the_reminder():

    message = "Hello guys, the professor Joji has started the poll"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={group_chat_reminder}&text={message}"
    # url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

    print(requests.get(url).json())