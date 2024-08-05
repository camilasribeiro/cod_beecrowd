#1051 - Imposto de Renda

salario = float(input())

if salario < 2000:
    print('Isento')
    
else:
    salario -= 2000

    if salario > 2500:
        soma = (1000 * 0.08) + (1500 * 0.18)
        salario -= 2500
        soma += salario * 0.28
        print(f'R$ {soma:.2f}')

    else:
        if salario > 1000:
            soma = (1000 * 0.08)
            salario -= 1000
            soma += salario * 0.18
            print(f'R$ {soma:.2f}')
        else: 
            soma = salario * 0.08
            print(f'R$ {soma:.2f}')
