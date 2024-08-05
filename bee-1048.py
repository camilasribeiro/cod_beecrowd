#1048 - Aumento de Salário

salario = float(input())

a = 15
b = 12
c = 10
d = 7
e = 4

if salario <= 800.00:
    if salario <= 400.00:
        reajuste = salario * (a/100)
        novo_salario = salario + reajuste
        print(f'Novo salario: {novo_salario:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: {a} %')
  
    else:
        reajuste = salario * (b/100)
        novo_salario = salario + reajuste
        print(f'Novo salario: {novo_salario:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: {b} %')
    
else:

    if salario <= 2000:
        if salario <= 1200:
            reajuste = salario * (c/100)
            novo_salario = salario + reajuste
            print(f'Novo salario: {novo_salario:.2f}')
            print(f'Reajuste ganho: {reajuste:.2f}')
            print(f'Em percentual: {c} %')

        else:
            reajuste = salario * (d/100)
            novo_salario = salario + reajuste
            print(f'Novo salario: {novo_salario:.2f}')
            print(f'Reajuste ganho: {reajuste:.2f}')
            print(f'Em percentual: {d} %')
            
    else:
        reajuste = salario * (e/100)
        novo_salario = salario + reajuste
        print(f'Novo salario: {novo_salario:.2f}')
        print(f'Reajuste ganho: {reajuste:.2f}')
        print(f'Em percentual: {e} %')
