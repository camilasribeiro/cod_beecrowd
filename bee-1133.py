#1133 - Resto da Divisão

x = int(input())
y = int(input())
for i in range(x+1,y):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
for i in range(y+1,x):
    if i % 5 == 2 or i % 5 == 3:
        print(i)
        