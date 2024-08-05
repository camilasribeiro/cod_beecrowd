#1064 - Positivos e Média

x = 6
cont = 0
positivos = 0
soma = 0

while cont < x:
    entrada = float(input())
    if entrada >= 0:
        positivos += 1
        soma += entrada
    cont += 1
        
media = soma / positivos
print(f'{positivos} valores positivos')
print(f'{media:.1f}')
