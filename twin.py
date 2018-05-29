m=int(raw_input())
n=list(raw_input().split())
new=[]
for i in n:
	i=int(i)
	new.append(i)
new.sort()
new.reverse()
#print new
new1=new[1:]
maxi=max(new)
su=sum(new)
total=su/2+1
j=0;k=0
#print total
'''if maxi>sum(new1):
	print "1"
else:'''
for i in new:
	i=int(i)
	#print i
	k=k+i
	j+=1
	#print k,i
	#new.remove(i)
	#print new
	if k>=total:
		break
print j
		
	

