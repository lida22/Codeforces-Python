m=int(raw_input())
n=list(raw_input().split())
new=[]
for i in n:
	i=int(i)
	new.append(i)
	
new.sort()
#print new
new.reverse()
#print new
k=0;j=0
if m<1:
	print"0"
else:
	for i in new:
		i=int(i)
		k=k+i
		#print k
		j+=1
		#print k
		if k>=m:
			break
		
	if k<m:
		print "-1"
	else:
		print j
	
	
