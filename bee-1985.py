#1985 - MacPRONALTS

qtd = int(input())

soma = 0

op1 = 1.50
op2 = 2.50
op3 = 3.50
op4 = 4.50
op5 = 5.50

for i in range(qtd):
    produto, quantidade = input().split()
    produto, quantidade = int(produto), int(quantidade)

    if produto == 1001:
        soma += op1 * quantidade
    elif produto == 1002:
        soma += op2 * quantidade
    elif produto == 1003:
        soma += op3 * quantidade
    elif produto == 1004:
        soma += op4 * quantidade
    elif produto == 1005:
        soma += op5 * quantidade

print(f'{soma:.2f}')
