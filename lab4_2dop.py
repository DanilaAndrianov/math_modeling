def fib(n):
    f1 = 1
    f2 = 2
    for i in range (3,n):
        b=f1
        f1=f2
        f2=b+f1
    return f2
print(fib(9999))
    