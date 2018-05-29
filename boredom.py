m=int(raw_input())
n=list(raw_input().split())
#a=max(n)
a=[]
for x,y in enumerate(n):
	#print x,y
	a=max(y),x
	s=a[1]
	if int(s)+1==x:
		del n[x]
	if int(s)-1==x:
		del n[x]
	print n

	#del n[x]
	#print n
	


	
