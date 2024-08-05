#1175 - Troca em Vetor I

N = 20 * [0]
pos = 0

while pos < 20:
    N[pos] = int(input())
    pos += 1

i = 0
f = 19

while i < 20 // 2:
    troca = N[i]
    N[i] = N[f]
    N[f] = troca
    i += 1
    f -= 1

pos = 0
while pos < 20:
    print(f'N[{pos}] = {N[pos]}')
    pos += 1
    