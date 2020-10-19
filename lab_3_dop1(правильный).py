import numpy as np
n=4
p=3
my_array1=np.zeros(shape=(n,p))
for (i,j), x in np.ndenumerate(my_array1):
    print(i, j, x, sep=';')
    m=input(f'введите значение: [{i},{j}]:' )
    my_array1[i,j]=float(m)
    print(my_array1)
my_array2=np.zeros(shape=(n,p))
for (i,j), x in np.ndenumerate(my_array2):
    print(i, j, x, sep=';')
    m=input(f'введите значение: [{i},{j}]:' )
    my_array2[i,j]=float(m)
print(my_array2)
my_array3=np.zeros(shape=(n,p))
for (i,j), x in np.ndenumerate(my_array3): 
    if my_array1[i,j]>my_array2[i,j]:
        my_array3[i,j]=my_array1[i,j]
    else:
        my_array3[i,j]=my_array2[i,j]
print('Max', my_array3)
        
