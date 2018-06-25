import sys
import time
import json

t1 = time.clock()
inputfile = open(sys.argv[1],'r',encoding = 'UTF-8')
namemapdict = json.load(inputfile)
keylist = []
valuelist = []
#print(namemapdict)

for key in namemapdict:
	keylist.append(key)
	valuelist.append(namemapdict[key])
inputfile.close()

def quicksort(k,v,start,end):
	if start >= end:
		return k,v
	mid = k[end]
	left = start
	right = end-1
	while left < right:
		while k[left] < mid and left < right:
			left += 1
		while k[right] >= mid and left < right:
			right -= 1
		k[left],k[right] = k[right],k[left]
		v[left],v[right] = v[right],v[left]
	if k[left] >= k[end]:
		k[left],k[end] = k[end],k[left]
		v[left],v[end] = v[end],v[left]
	else:
		left += 1
	k,v = quicksort(k,v,start,left-1)
	k,v = quicksort(k,v,left+1,end)
	return k,v

keylist, valuelist = quicksort(keylist,valuelist,0,len(keylist)-1)

commonindex = []
diffstring = []
for i in range(len(keylist)):
	N = 0
	if len(keylist[i]) >= len(valuelist[i]):
		N = len(valuelist[i])
	else:
		N = len(keylist[i])
	idx = 0
	modify = ""
	flag = False
	for j in range(N):
		if keylist[i][j] != valuelist[i][j] and not flag:
			break
		idx += 1
	for j in range(idx,len(valuelist[i])):
		modify += valuelist[i][j]
	commonindex.append(idx)
	diffstring.append(modify)

outputfile = open(sys.argv[2],'w')
outputfile.write("import sys\n")
outputfile.write("import json\n")
outputfile.write("d = {")
for i in range(len(keylist)):
	outputfile.write(str(i)+":")
	if len(diffstring[i]) == 0 and len(keylist[i]) == len(valuelist[i]):
		outputfile.write("\"\"")
	else:
		outputfile.write("("+str(commonindex[i])+",\""+diffstring[i]+"\")")
	if i != len(keylist)-1:
		outputfile.write(",")
outputfile.write("}\n")

outputfile.write("import time\n")
outputfile.write("t1=time.clock()\n")
outputfile.write("f=open(sys.argv[1],'r',encoding='UTF-8')\n")
outputfile.write("n=json.load(f)[0]\n")
outputfile.write("f.close()\n")
outputfile.write("n.sort()\n")
outputfile.write("f=open(sys.argv[2],'w')\n")
outputfile.write("f.write(\"{\\n\")\n")
outputfile.write("for i in range(len(n)):\n")
outputfile.write("\tif len(d[i])==0:\n")
outputfile.write("\t\tf.write('\\\"'+n[i]+'\\\":\\\"'+n[i]+'\\\"')\n")
outputfile.write("\telse:\n")
outputfile.write("\t\tf.write('\\\"'+n[i]+'\\\":\\\"'+n[i][0:d[i][0]]+d[i][1]+'\\\"')\n")
outputfile.write("\tif i!=len(n)-1:\n")
outputfile.write("\t\tf.write(\",\")\n")
outputfile.write("\tf.write(\"\\n\")\n")
outputfile.write("f.write(\"}\")\n")
outputfile.write("f.close()\n")
outputfile.write("t2=time.clock()\n")
outputfile.write("print(\"Mapping Time Usage: \"+str(t2-t1)+\" seconds.\")\n")
outputfile.close()

t2 = time.clock()
print("Create Python Script Time Usage: "+str(t2-t1)+" seconds.")
