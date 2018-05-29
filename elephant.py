num=int(raw_input())
l=[]
r=0
for i in range(0,num):
   l.append(1)
#print l 
while(len(l)>1):
  if(len(l)>=5):
   r=r+1
   for i in range(1,5):
         del(l[0])
  elif(len(l)>=4):
    r=r+1
    for i in range(0,4):
         del(l[0])
  elif(len(l)>=3):
    r=r+1
    for i in range(0,3):
         del(l[0])
  elif(len(l)>=2):
    r=r+1
    for i in range(0,2):
         del(l[0])
  elif(len(l)>=1):
    r=r+1
    for i in range(1):
         del(l[0])
  else:
    break

print r
   

	
 


