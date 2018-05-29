chat=raw_input().split()
print len(chat)
w=[]
if len(chat)>5:
	for i in chat:
		w.append(i)
		print w      
		if i == "h" and i == "e" and i == "l" and i == "o":
			x="YES"	
		else:
			x="NO"
	print x
else:
	print "no"

   
