m,n=map(int,raw_input().split())
anb=m/n
b=m%n
#print anb,b
ans=anb+b
#print ans
an=ans
k=0
ab=[]
c=[]
d=[]
if m<n:
	print m
elif ans>=n:
	while ans>=n:
		a=ans/n
		b=ans%n
		#ab.append(a)
		ans=b+a
		
		c.append(a)
		#print c
		#ans=ans1
		
		#d.append(ans)
		#print d
	#print ans
	#print sum(ab)
	#print sum(c)
	cc=sum(c)	
	#print ans
	ans1=m+cc+anb
	print ans1
else:
	ans1=anb+m
	print ans1
