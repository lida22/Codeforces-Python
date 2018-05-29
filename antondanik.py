a=int(raw_input())
b=raw_input()
ans=b.count('A')
ans1=b.count('D')
if ans>ans1:
	print "Anton"
if ans<ans1:
	print "Danik"
if ans==ans1:
	print "Friendship"
