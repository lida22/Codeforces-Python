from collections import Counter
st1=raw_input()
st2=raw_input()
st3=raw_input()
ans=st1+st2
if Counter(ans) == Counter(st3):
	print "YES"
else:
	print "NO"
