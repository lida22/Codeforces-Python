word=raw_input()
count=1
length=""
for i in range(1,len(word)):
    if word[i-1]==word[i]:
       count+=1
    else :
        length += str(count)+", "
        count=1
length += (str(count))
#print (length)
s=length.split(",")
for i in s:
	#print int(i)
	if int(i)>=7:
		x="YES"
		break
	else:
		x="NO"
print x








