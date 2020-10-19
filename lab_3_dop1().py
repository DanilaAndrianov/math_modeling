a = []
N = 5
for i in range(N):
    num = int(input())
    a.append(num)
print(a)
num = int(input("Число: "))
j = int(input("Позиция: "))
 
a.insert(j-1,num)
 
print(a)