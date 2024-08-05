#1072 - Intervalo 2

entrada = int(input())
contagem = 0
i = 0
o = 0

while contagem < entrada:
    x = int(input())
    if x >= 10 and x <= 20: 
        i += 1
    else: 
        o += 1
    contagem += 1

print(i, 'in')
print(o, 'out')
