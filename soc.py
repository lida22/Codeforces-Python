m,n=map(int,raw_input().split())
ans=min(m,n)
#print ans
a=max(m,n)
aa=a-ans
#print aa
if aa>=2:
	ans1=aa/2
else:
	ans1=0
print ans, ans1
