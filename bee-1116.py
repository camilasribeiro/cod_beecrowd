#1116 - Dividindo X por Y

qtd = int(input())
cont = 0
while cont < qtd:
    x, y = input().split()
    x, y = int(x), int(y)
    if y != 0:
        print(x/y)
    else:
        print('divisao impossivel')
    cont += 1
