#1038 - Lanche

cod, qtd = input().split()
cod, qtd = int(cod), int(qtd)

a = 4.00
b = 4.50
c = 5.00
d = 2.00
e = 1.50

if cod == 1: t = qtd * a
if cod == 2: t = qtd * b
if cod == 3: t = qtd * c
if cod == 4: t = qtd * d
if cod == 5: t = qtd * e
    
print(f'Total: R$ {t:.2f}')
