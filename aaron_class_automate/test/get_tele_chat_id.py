import requests

TOKEN = "5663501363:AAEQtcQd2AM-vuVecfd1doHFDLLNl_hbOyM"
chat_id = "1123696380"

message = "hello"

# url = f"https://api.telegram.org/bot{TOKEN}/sendMessage?chat_id={chat_id}&text={message}"
url = f"https://api.telegram.org/bot{TOKEN}/getUpdates"

print(requests.get(url).json())

