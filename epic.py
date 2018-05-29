x,y,p=map(int,raw_input().split())
while x!=y:
		if x<=0:
			x +=y
		elif y<=0:
			y +=x
		elif x>y:
			x -=y
		else:
			y -=x
print "gcd is" ,x
