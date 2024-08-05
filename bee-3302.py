#3302 - Resposta Certa

n = int(input())
pos = 0
num = 1
lista = n *[0]

while pos < n:
    lista[pos] = int(input())
    print(f'resposta {num}: {lista[pos]}')
    pos += 1
    num += 1
    