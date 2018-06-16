import sys

d1 = {}
d2 = {}

f1 = open(sys.argv[1],'r',encoding = 'UTF-8')
while True:
	l = f1.readline()
	l = l.strip().replace(',','')
	if l == "":
		break
	if l[0] != "{" and l[0] != "}":
		ll = l.split(':')
		k1 = ll[0].strip().replace('\"','')
		v1 = ll[1].strip().replace('\"','')
		d1[k1]=v1
f1.close()

f2 = open(sys.argv[2],'r',encoding = 'UTF-8')
while True:
	l = f2.readline()
	l = l.strip().replace(',','')
	if l == "":
		break
	if l[0] != "{" and l[0] != "}":
		ll = l.split(':')
		k2 = ll[0].replace('\"','')
		v2 = ll[1].replace('\"','')
		d2[k2]=v2
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
else:
	print("The results are the same. ------------> Successful!!")
print()
