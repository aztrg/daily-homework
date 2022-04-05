def fun(n):
    a = n % 10
    b = n // 10 % 10
    c = n // 100 % 10
    d = n // 1000
    if a ** 4 + b ** 4 + c ** 4 + d ** 4 == n ** 4:
        return True
    else:
        return


n = int(input('输入一个四位数'))
if (fun(n)):
    print('%d是四叶玫瑰数' % n)
else:
    print('%d不是四叶玫瑰数' % n)
