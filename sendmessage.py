import requests

def send(caption, photourl):
    bot_token = ""
    chatid = ""



    baseline = "https://api.telegram.org/bot" + bot_token + "/sendPhoto"
    params = {"chat_id": str(chatid), "caption": caption, "photo": photourl}
    req = requests.get(baseline, params)
    if str(req.status_code) == "200":
        return True
    else:
        return req.status_code