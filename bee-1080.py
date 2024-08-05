#1080 - Maior e Posição

valores = []
valor = 0
for i in range(100):
    valor = int(input())
    valores.append(valor)

maior = valores[0]
posicao = 0

for i in range(1, 100):
    if valores[i] > maior:
        maior = valores[i]
        posicao = i + 1

print(maior)
print(posicao)
