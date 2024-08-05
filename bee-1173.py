#1173 - Preenchimento de Vetor I

a = int(input())
lista = 10 * [0]
pos = 0

while pos < 10:
    lista[pos] = a
    print(f'N[{pos}] = {lista[pos]}')
    a+= a
    pos += 1
