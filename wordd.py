word=raw_input()
count=0
count2=0
for i in word:
	if i.isupper():
		count+=1
	if i.islower():
		count2+=1
if count>count2:
	print word.upper()
if count<count2:
	print word.lower()
if count==count2:
	print word.lower()

