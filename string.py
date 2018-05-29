wrd=raw_input()
e=[]
new=wrd.lower()
#print new
#newstr = ""
vowels = ('a', 'e', 'i', 'o', 'u', 'y')
for x in new:
	if x not in vowels:
            e.append(x) 
print "."+'.'.join(e)

