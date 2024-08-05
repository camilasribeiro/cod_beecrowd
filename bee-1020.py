#1020 - Idade em Dias

idade = int(input())
ano = 0
mes = 0
dia = 0

while idade > 365:
    idade -= 365
    ano += 1
while idade >= 30:
    idade -= 30
    mes += 1
    if idade < 30:
        dia = idade
            
print(f'{ano} ano(s)')
print(f'{mes} mes(es)')
print(f'{dia} dia(s)')
