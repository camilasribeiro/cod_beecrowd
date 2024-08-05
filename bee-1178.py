#1178 - Preenchimento de Vetor III

valor = float(input())
N = 100 * [0]

N[0] = valor
print(f'N[0] = {N[0]:.4f}')
pos = 1

while pos < 100: 
    N[pos] = (N[pos-1] / 2)
    print(f'N[{pos}] = {N[pos]:.4f}')
    pos += 1
