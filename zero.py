m=int(raw_input())
s=list(raw_input())
#print s
k=0;l=0
if len(s)==1 or len(set(s)) == 1 :
	print m

elif len(s)==2:
	for i,j in zip(s, s[1:]):
		if i=="1" and j=="0":
			print "0"
		elif i=="0" and j=="1":
			print "0"
		else:
			print len(s)

else:
	while k<len(s)+1:
		#print "j",s
		for i,j in zip(s, s[1:]):
			#print i,j
			if i!=j and len(s)>1:
				s.remove(i)
				s.remove(j)
				f=len(s)
				#print s
			if len(set(s)) == 1:
				f=len(s)
				break
	

		k+=1
	print f
	#print len(s)
	

'''elif i=="0" and j=="1" and len(s)>1:
				#print "j"
				s.remove(i)
				s.remove(j)
				print s
			else:
				print s
		k+=1
	else:
				if len(s)>1:
					if i=="0" and j=="1":
						s.remove("0")
						s.remove("1")'''

	#print s	

