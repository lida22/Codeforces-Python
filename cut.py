m,n,p,q=map(int,raw_input().split())
if n==p==q==m:
	print "1"
elif n+p==m:
	print "2"
elif p+q==m:
	print "2"
elif n+q==m:
	print "2"
elif n+p+q==m:
	print "3"
else:
	print m
