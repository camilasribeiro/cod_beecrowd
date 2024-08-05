#2416 - Corrida

metros, comprimento_pista = input().split()
metros, comprimento_pista = int(metros), int(comprimento_pista)

ponto_termino = metros % comprimento_pista

print(ponto_termino)
