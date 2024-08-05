#1177 - Preenchimento de Vetor II

x = int(input())

N = 1000  * [0]
pos = 0
num = 0

while pos < 1000:
    N[pos] = num
    num += 1
    if num == x:
        num = 0
    pos += 1

pos = 0
while pos < 1000:
    print(f'N[{pos}] = {N[pos]}')
    pos += 1
