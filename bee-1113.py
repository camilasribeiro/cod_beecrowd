#1113 - Crescente e Decrescente

while True:
    x, y = input().split()
    x, y = int(x), int(y)

    if x == y:
        break
    
    if x < y: print('Crescente')
    else: print('Decrescente')
    