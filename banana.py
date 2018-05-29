k,n,w=map(int,raw_input().split())
h=0
tl=0
for i in range(1, w+1):
		h=h +i*k
		tl=h-n
		if h<n:
			u=0
			tl=u
print tl
		
