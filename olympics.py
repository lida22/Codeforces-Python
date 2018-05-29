m,n=map(int,raw_input().split())
list1=list(raw_input().split())
k=0
g=0
for i in list1:
	i=int(i)
	if (5-i)>=n:
		k+=1
if k%3==0:
	ans= k/3
	print ans
elif k>3:
	for i in range(1, k+1):
		if i%3==0:
			g+=1
	print g
else:
	print "0"
			

	

		
