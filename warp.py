import requests
import json
import datetime
import random
import string
idwarp = "Copy id rồi bỏ vào đây"


def genString(stringLength):
    letters = string.ascii_letters + string.digits
    return ''.join(random.choice(letters) for i in range(stringLength))



def chay():
    install_id = genString(11)
    body = {"key": "{}=".format(genString(42)),
            "install_id": install_id,
            "fcm_token": "{}:APA91b{}".format(install_id, genString(134)),
            "referrer": idwarp,
            "warp_enabled": False,
            "tos": datetime.datetime.now().isoformat()[:-3] + "+07:00",
            "type": "Android",
            "locale": "zh-CN"}

    bodyString = json.dumps(body)

    headers = {'Content-Type': 'application/json; charset=UTF-8',
               'Host': 'api.cloudflareclient.com',
               'Connection': 'Keep-Alive',
               'Accept-Encoding': 'gzip',
               'User-Agent': 'okhttp/3.12.1'
               }

    requests.post("https://api.cloudflareclient.com/v0a745/reg", data=bodyString, headers=headers)

while(1):
      chay()
