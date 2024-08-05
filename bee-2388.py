#2388 - Tacógrafo

qtd_int = int(input())

cont = 0
soma = 0

while cont < qtd_int:
    tempo, velocidade = input().split()
    tempo, velocidade = int(tempo), int(velocidade)
    soma += tempo * velocidade
    cont += 1

print(soma)
