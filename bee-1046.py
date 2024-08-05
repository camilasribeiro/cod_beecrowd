#1046 - Tempo de Jogo

a, b = input().split()
a, b = int(a), int(b)

if a == b:
    d = 24
elif b >= a:
    d = b - a
else:
    d = (b + 24) - a

print(f'O JOGO DUROU {d} HORA(S)')
