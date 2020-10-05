a=int(input('число'))
b=2
while a>0:
     if a%b==0:
         a=a/b
         print(b)
         b=2
     else:
         while a%b!=0:
             b+=1
     if a==1:
         print(1)
         break
        