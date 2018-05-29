n=int(raw_input())
f=[]
g=[]
y=[]
k=0
v=0
b=0
for i in range(n):
	m=map(int,raw_input().split(' '))
	f.append(m)
for i in f:
	#for j in i:
	u=i[0]
	b=i[1]
	g.append(u)
	y.append(b)
x=0
for j in range(len(y)):
	#print y[j]
	if g[j]>y[j]:
		k+=1
	if g[j]<y[j]:
		v+=1
	else:
		b=0
if k>v:
	print"Mishka"
if k<v:
	print"Chris"
if k==v:
	print"Friendship is magic!^^" 
		
'''
while x<len(g):
	for i in range(len(g)):
		print g[i]
		for j in range(len(y)-1):
			print y[j]
			if g[i]<y[j]:
				k+=1
				print k
				i+=1
				j+=1
	x+=1
		#else:
		#	v+=1
			#j+=1
'''
#print k,v
