string1=raw_input()
string2=raw_input()
a=string1.lower()
b=string2.lower()
if len(string1)==len(string2):
	if a>b:
		print 1
	elif a<b:
		print -1
	elif a==b:
		print 0
