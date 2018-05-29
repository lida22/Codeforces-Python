num=int(raw_input())
new=[]
new=map(int,raw_input("").split())
x=new[0]
y=new[1:]
#print y
new2=[]
new2=map(int,raw_input("").split())
z=new2[1:]
s=z+y
b=[]
#print s
for i in s:
    if i not in b:
        b.append(i)
b.sort()
g=[]
for i in range(1, num+1):
	g.append(i)
	if g==b:
		p="I become the guy."
	else:
		p="Oh, my keyboard!"
print p

