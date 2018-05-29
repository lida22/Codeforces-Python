m=int(raw_input())
n=list(raw_input().split())
k=[]
#print n
#maxii=max(n)
maxi= 0
for i in n:
	i=int(i)
	if i > maxi:
	    maxi=i
#print(maxi)
for i in n:
	i=int(i)
	j=int(maxi)-i
	#j=abs(j)
	k.append(j)
#print k
#print len(k)
print sum(k)


