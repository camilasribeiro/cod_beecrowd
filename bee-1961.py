#1961 - Pula Sapo

altura_pulo, qtd_canos = map(int,input().split())

lista = list(map(int, input().split())) 

fim_jogo = False
    
for i in range(qtd_canos - 1):
    calculo = abs(lista[i+1] - lista[i])
    if calculo > altura_pulo:
        print('GAME OVER')
        fim_jogo = True
        break
    
if not fim_jogo:
    print('YOU WIN')
    