#2172 - Evento

aumento, valor = input().split()
aumento, valor = int(aumento), int(valor)

while aumento != 0 and valor != 0:
    exp = aumento * valor
    print(exp)
    aumento, valor = input().split()
    aumento, valor = int(aumento), int(valor)
