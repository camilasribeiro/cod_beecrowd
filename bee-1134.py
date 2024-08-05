#1134 - Tipo de Combustível

x = int(input())
alcool = 0
gasolina = 0
diesel = 0
while x != 4:
    if x == 1:
            alcool += 1
    elif x == 2:
            gasolina += 1
    elif x == 3:
            diesel += 1
    x = int(input())
print('MUITO OBRIGADO')
print('Alcool:',alcool)
print('Gasolina:',gasolina)
print('Diesel:',diesel)
