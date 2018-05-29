a=int(raw_input())
b=[]
k=0
for i in range(a):
	b.append(raw_input())
	#b=b.split(",")
#print b
aa=''.join(b)
bb=list(str(aa))
if len(bb)==2:
	print "1"
else:
	for x,y in zip(bb,bb[1:]):
		#print x,y
		if x==y:
		#	print x,y
			k+=1
	print k+1
		


