z=int(raw_input())
y=[]
y=list(raw_input().split())
k=0
if sorted(y) == y:
	print "0"
else:
	for x, j in zip(y, y[1:]):
		print x,j
		while x<j:
			x, j=j, x
			k+=1
			print x,j
		while x>j:
			x, j=j, x
			print x,j
			k+=1
	print k
