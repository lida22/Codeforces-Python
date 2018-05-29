a=int(raw_input())
b=int(raw_input())
c=int(raw_input())
sol1=a+(b*c)
sol2=a*(b+c)
sol3=a*b*c
sol4=(a+b)*c
sol5=a+b+c



ans=max(sol1,sol2,sol3,sol4,sol5)
print ans
