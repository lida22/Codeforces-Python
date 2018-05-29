a=int(raw_input())
g=raw_input()
#print len(g)
b=g.lower()
c=set(b)
#print len(c),len(b)
if len(g)<26:
	print "NO"
if len(g)>=26:
	if len(c)==26:
		print "YES"
	else:
		print "NO"


