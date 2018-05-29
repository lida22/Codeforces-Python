''''year=raw_input()
while(True):
	year=str(int(year)+1)
	if(len(set(year))==4):
		g=year'''
def magic(year):
    while(True):
        year = str(int(year)+1)
        if(len(set(year))==4):
            return year


print magic(raw_input())



