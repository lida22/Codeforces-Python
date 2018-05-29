n,m,a,b=map(int,raw_input().split(" "))

check=b/m
#print check
g=0
if check>=a:
	rr=n*a
	print rr
elif m>n and a*n>=b:
	print b
elif m>n and a*n<b:
	print a
elif check<a and a<=b:
	r1=n-m
	#print r1
	if r1<m:
		#print "B"
		r1=n-m
		n=r1
		g+=b
		r3=n*a
		#print n,a
		re=g+r3
		print re
	while r1>=m:
		#print "B"
		r1=n-m
		n=r1
		g+=b
		if r1<m:
			#print "j"
			r3=n*a
			#print n,a
			r=g+r3
			print r

elif a>b and n%m>0:
	print (n/m)*b+b
if a>b and n%m==0:
	print (n/m)*b

	
		

		
	
		
