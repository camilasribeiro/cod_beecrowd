#1164 - Número Perfeito

N = int(input())
lista = N * [0]

pos = 0

while pos < N:
    lista[pos] = int(input())
    pos += 1

pos = 0

while pos < N:
    div = 1
    soma = 0

    while div < lista[pos]:
        if lista[pos] % div == 0:
            soma += div
        div += 1

    if soma == lista[pos]:
        print(lista[pos], 'eh perfeito')
    else:
        print(lista[pos], 'nao eh perfeito')
    
    pos += 1
    