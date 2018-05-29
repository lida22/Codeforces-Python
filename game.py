inp=int(raw_input())
inp2=raw_input().split()
'''s=[]
for i in inp2:
	i=int(i)'''
inp2 = [int(x) for x in inp2]
inp2.sort()
print ' '.join(str(x) for x in inp2)

