#1174 - Seleçao em Vetor I

lista = 100 * [0.0]
pos = 0

while pos < 100:
    a = float(input())
    lista[pos] = a
    if lista[pos] <= 10:
        print(f'A[{pos}] = {lista[pos]}')
    pos += 1
        