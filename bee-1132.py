#1132 - Múltiplos de 13

x = int(input())
y = int(input())

soma = 0

for i in range(x, y+1):
    if i % 13 != 0:
        soma += i

for i in range(y, x+1):
    if i % 13 != 0:
        soma += i

print(soma)
