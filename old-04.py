import hashlib
from random import *
from multiprocessing import Process
import os

def work(start, end):
	f = open("rainbowtable/rainbow_"+str(start)+".txt", "w")
	for j in range(start,end):
		data = str(j)+"salt_for_you"
		for i in range(0,500):
			data_sha1 = hashlib.sha1(data.encode('utf-8')).hexdigest()
		f.write(data+" : "+data_sha1[0:8]+"\n")
	f.close()

if __name__ == "__main__":
	if not os.path.isdir('rainbowtable'):
		os.mkdir('rainbowtable')

	pr1 = Process(target=work, args=(10000000,20000000))
	pr2 = Process(target=work, args=(20000000,30000000))
	pr3 = Process(target=work, args=(30000000,40000000))
	pr4 = Process(target=work, args=(40000000,50000000))
	pr5 = Process(target=work, args=(50000000,60000000))
	pr6 = Process(target=work, args=(60000000,70000000))
	pr7 = Process(target=work, args=(70000000,80000000))
	pr8 = Process(target=work, args=(80000000,90000000))
	pr9 = Process(target=work, args=(90000000,100000000))
	
	pr1.start()
	pr2.start()
	pr3.start()
	pr4.start()
	pr5.start()
	pr6.start()
	pr7.start()
	pr8.start()
	pr9.start()
	
	pr1.join()
	pr2.join()
	pr3.join()
	pr4.join()
	pr5.join()
	pr6.join()
	pr7.join()
	pr8.join()
	pr9.join()