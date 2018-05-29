m,n=map(int,raw_input().split())
k=0
for i in range(1, 100):
	m=m*3
	n=n*2
	k+=1
	if m>n:
		break
print k
		

