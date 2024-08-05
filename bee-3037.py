#3037 - Jogando Dardos Por Distância

casos_teste = int(input())

for i in range(casos_teste):
    joao = 0
    maria = 0

    for i in range(3):
        x, d = map(int, input().split())
        joao += x * d

    for i in range(3):
        x, d = map(int, input().split())
        maria += x * d
        
    if joao > maria: print('JOAO')
    else: print('MARIA')
