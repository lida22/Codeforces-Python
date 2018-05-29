x=int(raw_input())
l1=[]
l2=[]
l3=[]
new=[]

for i in range(0, x):
	k=0
	m,n,p=map(int,raw_input().split())
	l1.append(m)
	l2.append(n)
	l3.append(p)
	if sum(l1)==0 and sum(l2)==0 and sum(l3)==0:
		x="YES"
	else:
		x="NO"
print x


