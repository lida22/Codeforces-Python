from collections import Counter
a=int(raw_input())
b=list(raw_input().split())
c=list(raw_input().split())
d=list(raw_input().split())
x=Counter(b)
y=Counter(c)
z=Counter(d)
a1=x-y
a2=y-z
#print a2
ans=list(set(b) - set(c))
ans1=list(set(c) - set(d))

if not ans and not ans1:
	an=a1.keys()
	an1=a2.keys()
	#print"g"
	print "".join(an)
	print "".join(an1)

elif not ans1:
	an1=a2.keys()
	#print"c"
	print "".join(ans)
	print "".join(an1)
elif not ans:
	an=a1.keys()
	#print"g"
	print "".join(an)
	print "".join(ans1)
else:
	#print"f"
	print "".join(ans)
	print "".join(ans1)
