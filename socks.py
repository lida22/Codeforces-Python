m,n=map(int,raw_input().split())
total=m
#k=0;a=0
while(m>=n):
	a=(m/n)
	total=total+a
	k=(m%n)
	m=(a+k)
print total
	
#m=m+k
#while m>1
