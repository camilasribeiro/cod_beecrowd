#1589 - Bob Conduite

testes = int(input())
cont = 0

while cont < testes:
    r1, r2 = input().split()
    r1, r2 = int(r1), int(r2)
    soma = r1 + r2
    print(soma)
    cont+= 1
