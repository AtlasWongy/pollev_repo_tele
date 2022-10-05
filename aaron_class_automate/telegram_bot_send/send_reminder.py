import requests

TOKEN = "5663501363:AAEQtcQd2AM-vuVecfd1doHFDLLNl_hbOyM"
yijie_chat_id = "127764571"
aaron_chat_id = "101064221"

def send_the_reminder():

    message = "Aaron, your professor has started the poll"

    url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={aaron_chat_id}&text={message}"
    # url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

    print(requests.get(url).json())