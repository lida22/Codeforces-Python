stop=int(raw_input())
s=0
y=0
for i in range(1, stop+1, 2):
	if stop%2==0:
		s=s+(-i)+(i+1)
	else:
		y=y+(-i)+(i+1)
			s=y-(i+1)
		
print s
