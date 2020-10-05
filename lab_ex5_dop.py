a=int(input('число '))
for b in range(2,a+1):
    s=0
    for t in range(1,b):
        if b%t==0:
            s+=t
    if s==b:
       print(b)
       