#1153 - Fatorial Simples

n = int(input())
cont = n - 1
while cont >= 1:
    n = n * cont
    cont -= 1

print(n)
