new=raw_input().strip("{").strip("}").split(",")
f=[]
gg=[]
for i in new:
	i=i.split()
	f.append(i)
for j in f:
	for k in j:
		gg.append(k)
#print gg
	
ot=set(gg)
#print ot
g="'".join(new)
#print len(g)
if len(g)==0:
	print "0"
else:
	print len(ot)
