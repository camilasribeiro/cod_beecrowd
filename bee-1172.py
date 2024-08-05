#1172 - Substituição em Vetor I

lista = 10 * [0]
pos = 0

while pos < 10:
    lista[pos] = int(input())
    pos += 1

pos = 0

while pos < 10:
    if lista[pos] <= 0:
        lista[pos] = 1
    print(f'X[{pos}] = {lista[pos]}')
    pos += 1
    