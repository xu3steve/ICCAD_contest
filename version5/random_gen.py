import sys
import random

f = open(sys.argv[1],'r',encoding = 'UTF-8')
count = 0
listkey = []
listvalue = []

print("Randomly Generate Testcase ...")

while True:
	count += 1
	i = f.readline()
	#if count > 10:
	#	break
	if i == "":
		break
	if i[0] != "{" and i[0] !=  "}":
		p = i.strip().replace(',','').split(':')
		k = eval(p[0].strip())
		v = eval(p[1].strip())
		listkey.append(k)
		listvalue.append(v)
f.close()

#print(listkey)
#print(listvalue)

f = open(sys.argv[2],'w')
NewRange = [i for i in range(len(listkey))]
NewRange2 = [i for i in range(len(listvalue))]
#NewRange = []
#NewRange2 = []
'''#print("Start random 1")
while len(NRange) != 0:
	rand = 9901
	for j in range(100):
		rand = (rand * 9689) % 9887
	rand = rand % len(NRange)
	NewRange.append(NRange[rand])
	del NRange[rand]
#print("Start random 2")
while len(NRange2) != 0:
	rand = 9239
	for j in range(100):
		rand = (rand * 9551) % 9929
	rand = rand % len(NRange2)
	NewRange2.append(NRange2[rand])
	del NRange2[rand]
'''

random.shuffle(NewRange)
random.shuffle(NewRange2)

#print("Start output")

f.write("[\n")
f.write(" [")
for i in range(len(NewRange)):
	f.write('\"'+listkey[NewRange[i]]+'\"')
	if i != len(listkey)-1:
		f.write(',')
f.write('],\n')

f.write(" [")
for i in range(len(NewRange2)):
	f.write('\"'+listvalue[NewRange2[i]]+'\"')
	if i != len(listvalue)-1:
		f.write(',')
f.write(']\n')
f.write("]")



