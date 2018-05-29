in1,in2=map(int,raw_input().split())
if in1%2==0:
	s=in1/2
else:
	s=(in1/2)+1
#print s
if s>=in2:
	ans=(in2*2)-1
else:
	k=in2-s
	ans=k*2
print ans
'''for i in xrange(1, in1+1):
	if i%2!=0:
		odd.append(i)
	if i%2==0:
		even.append(i)
ans=odd+even
ans.insert(0,0)
for i in range(2, len(ans)):
	
	s=ans[in2]
print s'''
		

