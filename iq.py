num=int(raw_input())
l=[]
l=map(int,raw_input().split())
tmp=0
for x in l:
	if x%2==0:
		res=l.index(x)
		#res+=1
	#if x%2!=0:
	#	res=x
#print res
for x in l:
	if x%2!=0:
		res=l.index(x)
		#res+=1
		print res
#tmp=res+1
print res


