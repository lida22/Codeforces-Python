s = input('enter the year')
print s
if s%4 == 0:
	if s%400 == 0 or s%100 != 0:
		print s, 'is a leap year'
	else:
		print 'it is not leap year'
else:
	print 'it is not a leap year'
