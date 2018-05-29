a=list(raw_input().split())
ans=[]
for i in a:
	i=int(i)
	ans.append(i)
ans=sorted(ans)
#print ans
	
#print a[0],a[1],a[2]
b=int(ans[1])-int(ans[0])
c=int(ans[2])-int(ans[1])
#print b,c
print b+c
	
