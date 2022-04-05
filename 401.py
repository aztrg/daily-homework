def Fun(x):
   if x%2==0 and x%7==0:
       return 1
   else:
       return 0
a=int(input('The starting value'))
b=int(input('The end value'))
s=0
for i in range(a,b):
   if Fun(i):
       s+=1
       print(i,end=' ')

print('\n满足条件的数有%d个'%s)
