x=int(raw_input())
y=[]
a=[]
k=0;l=0
#y=range(3)
for i in range(0, x):
	#i=0
	y.append(raw_input().split())
for i in y:
	for j in i:
		if j=='1':
			k+=1
	a.append(k)
	k=0
#print a
for m in a:
	if m>1:
		l+=1
print l
	
