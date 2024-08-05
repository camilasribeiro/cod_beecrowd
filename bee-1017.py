#1017 - Gasto de Combustível

horas = int(input())
velocidade = int(input())
litros = 12
velocidademedia = horas * velocidade
litrosgastos = velocidademedia / litros
print(f'{litrosgastos:.3f}')
