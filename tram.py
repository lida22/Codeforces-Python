stop=int(raw_input())
y=[]
new=[]
s=0
for i in range(0, stop):
	y.append(raw_input().split())
tram=[]
for i in range(stop):
	s=s+ int(y[i][1]) - int(y[i][0])
	tram.append(s)
print max(tram)
