value=int(raw_input())
y=[]
X=0
for i in range(0, value):
	y.append(raw_input())
	if y[i]=="X++" or y[i]=="++X":
		X+=1
	if y[i]=="X--" or y[i]=="--X":
		X-=1
	if y[i]=="X++" and y[i]=="X--":
		X+=1
		X-=1
print X























	

