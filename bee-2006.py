#2006 - Identificando o Chá

num = int(input())

a, b, c, d, e = input().split()
a, b, c, d, e = int(a), int(b), int(c), int(d), int(e)

lista = [a, b, c, d, e]
cont = 0

for i in lista:
    if i == num:
        cont += 1

print(cont)
