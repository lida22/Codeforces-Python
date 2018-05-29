x=raw_input()
x=x.split(" ")
#print x
y=raw_input()
y=y.split(" ")
position=int(x[1])
r=int(x[0])
j=0
for i in range(0, len(y)):
	if int(y[i])>=int(y[position-1]):
		if int(y[i])>0:
			#print y[i]
			j+=1
print j	
			
	
