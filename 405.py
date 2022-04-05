def sortnum(m,n):
    if m>n:
        m,n=n,m
    else:
        m,n=m,n
    return m,n
m=int(input('please input a number:'))
n=int(input('please input another number:'))
print('从小到大排序为 %d %d'%sortnum(m,n))





