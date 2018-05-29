num=raw_input().split('+')
for item in num:
    item=int(item)
num.sort()
#print num
num = ['+'.join(num)]
num=''.join(map(str,num))
print num

