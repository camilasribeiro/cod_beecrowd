#1018 - Cédulas

N = int(input())
valor = N
n100 = 0
n50 = 0
n20 = 0
n10 = 0
n5 = 0
n2 = 0
n1 = 0

while valor >= 100:
    valor -= 100
    n100 += 1
    
while valor >= 50:
    valor -= 50
    n50 += 1
    
while valor >= 20:
    valor -= 20
    n20 += 1
    
while valor >= 10:
    valor -= 10
    n10 += 1
    
while valor >= 5:
    valor -= 5
    n5 += 1
    
while valor >= 2:
    valor -= 2
    n2 += 1
    
while valor >= 1:
    valor -= 1
    n1 += 1

print(N)
print(f'{n100} nota(s) de R$ 100,00')
print(f'{n50} nota(s) de R$ 50,00')
print(f'{n20} nota(s) de R$ 20,00')
print(f'{n10} nota(s) de R$ 10,00')
print(f'{n5} nota(s) de R$ 5,00')
print(f'{n2} nota(s) de R$ 2,00')
print(f'{n1} nota(s) de R$ 1,00')
