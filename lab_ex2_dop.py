a=int(input('a='))
b=int(input('b='))
c=int(input('c='))
if (a+b>c) and (a+c>b) and (b+c>a):
    print('существует')
    if (a==b==c):
         print('равносторонний')
    elif (a==b) or (a==c) or (c==b):
         print('равнобедренный')
    elif (a>b>c):
         print('разносторонний')
else:
    print('не существует')
     