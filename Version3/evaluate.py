import sys
import json

d1 = {}
d2 = {}

f1 = open(sys.argv[1],'r',encoding = 'UTF-8')
n = json.load(f1)
for i in n:
	d1[i] = n[i]
f1.close()
f2 = open(sys.argv[2],'r',encoding = 'UTF-8')
n = json.load(f2)
for i in n:
	d2[i] = n[i]
f2.close()
	
count = 0
error = 0
for i in d1:
	count += 1
	if d1[i] != d2[i]:
		#print("count "+str(count)+": Error")
		print("The Error term")
		print("The Key       :"+i)
		print("Connect Answer:"+d1[i])
		print("My Answer     :"+d2[i])
		error += 1
	#else:
	#	print("count "+str(count)+": Correct")
#print("Total error:"+str(error))
if error > 0:
	print("The results are not the same. --------> Failure...")
	print("Error term: "+str(error)+" ,total term: "+str(count))
else:
	print("The results are the same. ------------> Successful!!")
print()
