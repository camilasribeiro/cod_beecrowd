#1043 - Triângulo

a, b, c = input().split()
a, b, c = float(a), float(b), float(c)

if (a + b) > c and (a + c) > b and (b + c) > a:
    perimetro = a + b + c
    print('Perimetro =',(perimetro))
else:
    area = (a + b) * c / 2
    print('Area =',(area))
    