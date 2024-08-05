#2061 - As Abas de Péricles

abas, qtd_acoes = input().split()
abas, qtd_acoes = int(abas), int(qtd_acoes)
cont = 0

while cont < qtd_acoes:
    acao = input()
    if acao == 'fechou':
        abas += 1
    else:
        abas -= 1
    cont += 1

print(abas)
