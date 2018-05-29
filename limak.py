m,n=map(int,raw_input().split())
h=[]
k=0
for i in range(1,m+1):
	#i+=5
	h.append(i*5)
#print h
s=0
for j in h:
	#print j
	s += j
	tmp=240-s
#	print tmp
	if (tmp)>=n:
		#j=j+(j+1)
#		print s
		k+=1
print k

		
