#1021 - Notas e Moedas

valor = float(input())

#notas

n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0

while valor >= 100:
    n100 += 1
    valor -= 100

while valor >= 50:
    n50 += 1
    valor -= 50

while valor >= 20:
    n20 += 1
    valor -= 20

while valor >= 10:
    n10 += 1
    valor -= 10
    
while valor >= 5:
    n5 += 1
    valor -= 5

while valor >= 2:
    n2 += 1
    valor -= 2

#moedas

m100 = 0
m50 = 0
m25 = 0
m10 = 0
m05 = 0
m01 = 0

valor = int(valor * 100)

while valor >= 100:
    m100 += 1
    valor -= 100

while valor >= 50:
    m50 += 1
    valor -= 50
    
while valor >= 25:
    m25 += 1
    valor -= 25
    
while valor >= 10:
    m10 += 1
    valor -= 10
    
while valor >= 5:
    m05 += 1
    valor -= 5
    
while valor >= 1:
    m01 += 1
    valor -= 1

print('NOTAS:')
print(f'{n100} nota(s) de R$ 100.00')
print(f'{n50} nota(s) de R$ 50.00')
print(f'{n20} nota(s) de R$ 20.00')
print(f'{n10} nota(s) de R$ 10.00')
print(f'{n5} nota(s) de R$ 5.00')
print(f'{n2} nota(s) de R$ 2.00')

print('MOEDAS:')
print(f'{m100} moeda(s) de R$ 1.00')
print(f'{m50} moeda(s) de R$ 0.50')
print(f'{m25} moeda(s) de R$ 0.25')
print(f'{m10} moeda(s) de R$ 0.10')
print(f'{m05} moeda(s) de R$ 0.05')
print(f'{m01} moeda(s) de R$ 0.01')
