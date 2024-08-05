#1943 - Top N

colocacao = int(input())

if colocacao == 1: print('Top 1')
elif colocacao > 1 and colocacao < 4: print('Top 3')
elif colocacao > 3 and colocacao < 6: print('Top 5')
elif colocacao > 5 and colocacao < 11: print('Top 10')
elif colocacao > 10 and colocacao < 26: print('Top 25')
elif colocacao > 25 and colocacao < 51: print('Top 50')
elif colocacao > 50 and colocacao < 101: print('Top 100')
