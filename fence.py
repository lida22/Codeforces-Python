m,n=map(int,raw_input().split())
lst=list(raw_input().split())
#print lst
k=0;p=0
for i in lst:
	i=int(i)
	if i>n:
		#print "ki"+i
		k+=2
	if i<=n:
		#print "l"+i
		p+=1
#print k,p
ans=k+p
print ans
