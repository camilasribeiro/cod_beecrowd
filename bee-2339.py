#2339 - Aviões de Papel

competidores, folhas, folhas_competidores = input().split()
competidores, folhas, folhas_competidores = int(competidores), int(folhas), int(folhas_competidores)

calculo = competidores * folhas_competidores

if calculo <= folhas: print('S')
else: print('N')
