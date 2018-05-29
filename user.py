import itertools
in1=raw_input()
in2=list(raw_input().split())
m=[];s=[]
k=0
for i in reversed(in2):
	m.append(i)
b=len(m)
#mylist = range(5)


for i in in2[1:]:
	
		#print in2[i]
		#print in2[:i+1]
		if in2[i]>in2[:i+1]:
			print in2[i]
			print in2[:i+1]
			k=int(k)+1
		print k
'''if in2[i+1]<in2[:i+1]:
		k+=1
	else:
		k="0"
print k'''
	
