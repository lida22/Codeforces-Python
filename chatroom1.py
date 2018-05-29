myString1 = raw_input()
c='l'
a='e'
b='o'
if myString1.count('h')>=1 and myString1.count('e')>=1 and myString1.count('l')>=2 and myString1.count('o')>=1:
	try1=[pos for pos, char in enumerate(myString1) if char == b]	
	#print try1
	ans=myString1.index('h')
	myString=myString1[ans:try1[-1]+1]
	#print myString
	no=[pos for pos, char in enumerate(myString) if char == c]
	no1=[pos for pos, char in enumerate(myString) if char == a]
	no2=[pos for pos, char in enumerate(myString) if char == b]

	if myString.count('h')>=1 and myString.count('e')>=1 and myString.count('l')>=2 and myString.count('o')>=1:
	
		first=int(no[0])
		last=int(no[-1])
		first1=int(no1[0])
		last1=int(no1[-1])
		last2=int(no2[-1])
		if myString.index('h')<first1<no[-2]<last<last2:
			print "YES"
		else:
			print "NO"
	else:
		print "NO"
else:
	print "NO"
#print no,no1,no2

#print myString.index('h'),first1,no[-2],last,last2
'''s= raw_input()
s.index("h")
print s
wordlist = list(s)               # option 1, 
wordlist = [ch for ch in s] 
#new=set(wordlist) 
#print new

for i,j in enumerate(wordlist):
	print i("h"),j'''


   
