num=int(raw_input())
wrd=raw_input()
new=[]
k=0
new=list(wrd)	
for x, y in zip(new, new[1:]):
	#print x,y
	if x==y:
		k+=1
print k
			

