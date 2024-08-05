#1099 - Soma de Ímpares Consecutivos II

n = int(input())
cont = 0
soma = 0

while cont < n:
    x, y = input().split()
    x, y = int(x), int(y)

    for i in range(x+1, y):
        if i % 2 != 0:
            soma += i

    for i in range(y+1, x):
        if i % 2 != 0:
            soma += i

    print(soma)
    cont += 1
    soma = 0
