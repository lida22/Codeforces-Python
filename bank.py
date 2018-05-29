n=raw_input()
d=list(n)
#print d
if int(n)>=0:
	print n
else:
	s=d[:-1]
	v=''.join(s)
	g=d.pop(-2)
	v2=''.join(d)
	if int(v)>int(v2):
		if v=='0':
			print "0"
		else:
			print v
	else:
		if v2=='-0':
			print "0"
		else:
			print v2
	#print v,v2
