#1144 - Sequência Lógica

n = int(input())

for i in range(1, n+1):
    primeiro_valor = i
    segundo_valor = primeiro_valor * primeiro_valor
    terceiro_valor = (primeiro_valor * segundo_valor) + 1
    
    print(f'{primeiro_valor} {segundo_valor} {(terceiro_valor-1)}')
    print(f'{primeiro_valor} {(segundo_valor+1)} {terceiro_valor}')
    