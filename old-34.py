import requests

url = "https://webhacking.kr/challenge/js-7/?"
cookie = {"PHPSESSID":"hjb4hev90d5u7q3ejvvgigllgq"}

def solve(): # script 분석해보면 if문 밖에 있는 다음과 같은 코드를 발견할 수 있다. - > location[b('0x1c', '4c%d')] = b('0x1d', 'llaF'); 복사 -> console 창에 붙여넣기 
    payload = "Passw0RRdd=1"
    res = requests.get(url=url+payload, cookies=cookie)
    if "old-34 Pwned!" in res.text:
        print("old-34 Pwned!")
    elif "already solve" in res.text:
        print("already solve")

if __name__ == "__main__":
    solve()
