a=int(raw_input())
b=list(raw_input().split())
#print b
i=0
k=0
while i<len(b):
	#print "hi"
	if b[i]=='-1':
		#print "hi",b[i]
		k+=1
		i+=1
	elif b[i]>0:
		print i
		n=i+1
		#n= int(b[i])+int(b[i+1])
		print n
	 	if b[n]>=0:
			f=int(b[i])+int(b[n])
			print f
			i+=f
			#i+=int(b[i])+
		#i+=int(b[i])+1
		else:
			i+=int(b[i])+1
print k
