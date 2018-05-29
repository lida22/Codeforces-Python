a=int(raw_input())
k=0;p=0
f=[]
if a ==1:
	print "1"
else:
	for i in range(1, a+1):
		#print i
		k=k+i
		p+=k
		#print k,p
		if p==a:
			ans=i
		if p>a:
			#print i,p,a
			f.append(i)
			break
	for i in f:
		i=int(i)
		ans=i-1
	print ans

