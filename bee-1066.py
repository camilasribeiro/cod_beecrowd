#1066 - Pares, Ímpares, Positivos e Negativos

par = 0
impar = 0
positivo = 0
negativo = 0
quantidade = 0

while quantidade < 5:
    a = int(input())

    if a % 2 == 0: par += 1
    else: impar += 1

    if a != 0:
        if a < 0: negativo += 1
        else: positivo += 1
    
    quantidade+= 1

print(f'{par} valor(es) par(es)')
print(f'{impar} valor(es) impar(es)')
print(f'{positivo} valor(es) positivo(s)')
print(f'{negativo} valor(es) negativo(s)')
