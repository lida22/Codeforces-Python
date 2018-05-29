m,n=map(int,raw_input().split())
new=[]
new1=[]
for j in range(m):
	b=list(raw_input().split())
	new.append(b)
	
for j in new:
	for k in j:
		new1.append(k)
#print new1
if "C" in new1:
	print "#Color"
elif "M" in new1:
	print "#Color"
elif "Y" in new1:
	print "#Color"
else:
	print "#Black&White"

'''for i in new1:
	print i
	if i=="C" or i=="M" or i=="Y": 
		clr="#Color"
		if i!="W" or i!="B" or i!="G":
			clr="#Color"
		else:
		
			clr="#Black&White"
	else:
		
		clr="#Black&White"
print clr'''
