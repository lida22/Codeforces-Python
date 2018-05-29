gen=raw_input()
b = []
for i in gen:
    if i not in b:
        b.append(i)
if len(b)%2 != 0:
	print "IGNORE HIM!"
else:
	print"CHAT WITH HER!"
