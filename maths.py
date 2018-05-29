no1=raw_input()
b=raw_input()
g=len(no1)
k=[]
for i in range(len(no1)):
	if no1[i]=="0" and b[i]=="0":
		k.append("0")
	if no1[i]=="0" and b[i]=="1":
		k.append("1")
	if no1[i]=="1" and b[i]=="1":
		k.append("0")
	if no1[i]=="1" and b[i]=="0":
		k.append("1")
print ''.join(k)
