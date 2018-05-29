m,n,a=map(int,raw_input().split())
b = n/a
c = m/a
if  n%a != 0:
	b = b+1
if m%a != 0:
	c =c+1
d =b*c
print d

