s = int(raw_input())
w=[]
total=[]
for i in range(0, s):
	w.append(raw_input())
	#print w[0][1]
	if len(w[i])>10:
		#print "y"
		ans= str(w[i][0]) 
		#print ans
		ans2=str(len(w[i])-2)
		#print ans2
		ans3=str(w[i][-1])
		#print ans3
		total= str(ans+ans2+ans3)
	else:
		total = w[i]
	print total



