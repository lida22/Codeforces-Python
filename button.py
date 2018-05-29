no=int(raw_input())
if no>1:
	ans=(no-1)*no
	ans1=(no/2)+ans
	ans2=ans1+ans-no
	print ans2
else:
	print "1"
