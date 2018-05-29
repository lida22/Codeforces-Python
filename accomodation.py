x=int(raw_input())
l1=[]
l2=[]
new=[]

for i in range(0, x):
	k=0
	m,n=map(int,raw_input().split())
	l1.append(m)
	l2.append(n)
	if l1==l2:
		k=0
	if l1<l2:
		x=l2[i]-l1[i]
		new.append(x)
	for h in new:
		#print h
		if int(h)>=2:
			#print "u"
			k+=1
print k

