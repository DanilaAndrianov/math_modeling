import numpy as np

n=int(input('кол-во строк'))
p=int(input('кол-во столбцов'))
my_array1=np.zeros(shape=(n,p))

my_array2=np.zeros(p)
for (i,j), x in np.ndenumerate(my_array1):
    print(i,j,x,sep=';')
    m=input(f'введите значение: [{i},{j}]:' )
    my_array1[i,j]=float(m)
    print(my_array1)
    
for (i,j), x in np.ndenumerate(my_array1):
    if my_array2[j]<my_array1[i,j]:
        my_array2[j]=my_array1[i,j]
print(my_array2)
        
 