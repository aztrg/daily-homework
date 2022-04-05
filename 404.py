sum=1
def multiply(m):
    global sum
    sum=sum*m
while True:
    n=int(input('输入一个整数,当输入零表明结束：'))
    if n==0:
        print(0)
        break


    else:
        multiply(n)
print('零前所有数乘积为{}'.format(sum))

