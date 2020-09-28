b1=int(input('первый член-'))
q=int(input('множетели-'))
n=int(input('кол-во членов-'))
for i in range(1,n,1):
    b=b1*q**(i)
    print(b, end=' ')
    
    