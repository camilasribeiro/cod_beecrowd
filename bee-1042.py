#1042 - Sort Simples

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)
lista1 = [a, b, c]
lista2 = [a, b, c]

lista1.sort()
for i in lista1:
    print(i)

print()

for i in lista2:
    print(i)
    