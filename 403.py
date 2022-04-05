'''函数power(m,n)用于计算整数m的n次方，默认计算m的平方。编写power( )函数，并调用。'''




def power(m,n=2):
    s=m**n
    return s
a=int(input('please input a number m'))
b=int(input('please input a number n'))
print('m的n次方为%d'%power(a,b))