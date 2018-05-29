word=raw_input()
t=word[0]
d=word[1:]
if word.isupper():
	print(word.lower())
elif t.islower() and d.isupper():
	print(word.capitalize())
elif len(word)==1 and t.islower():
	print(word.upper())
else:
	print word
#print s
	
	
