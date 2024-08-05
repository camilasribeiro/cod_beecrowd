#1036 - Fórmula de Bhaskara

a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

d = b**2 - 4 * (a*c)

if a == 0:
    print('Impossivel calcular')
elif d >= 0:
    r1 = (-b + (d ** 0.5)) / (2 * a)
    r2 = (-b - (d ** 0.5)) / (2 * a)
    print(f'R1 = {r1:.5f}')
    print(f'R2 = {r2:.5f}')
else:
    print('Impossivel calcular')
    