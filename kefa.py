z=int(raw_input())
y=[]
y=list(raw_input().split())
k=1
ans=[]
if sorted(y) == y:
	print len(y)
else:
	for x, z in zip(y, y[1:]):
		x=int(x)
		z=int(z)
		if x<=z:
			k+=1
			ans.append(k)
		if x>z:
			
			k=1
	#print ans
	#print max(ans)
	#print k
	if not ans:
		print k
	elif max(ans)>=k:
		#print "k"
		print max(ans)
	else:
		#print "l"
		print k
	

'''for i in range(len(y)-1):
    		if y[i]<=y[i+1]:
			print y[i],y[i+1]
           		k+=1
	print k'''

