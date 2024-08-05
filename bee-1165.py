#1165 - Número Primo

N = int(input())
lista = N * [0]
pos = 0

while pos < N:
    lista[pos] = int(input())
    pos += 1

pos = 0

while pos < N:
    div = 1
    total_div = 0
    
    while div <= lista[pos]:
        if lista[pos] % div == 0:
            total_div += 1
        div += 1

    if total_div == 2:
        print(lista[pos], 'eh primo')
    else:
        print(lista[pos], 'nao eh primo')
    
    pos += 1
    