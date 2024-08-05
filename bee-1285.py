#1285 - Dígitos Diferentes

while True:
    try:
        n, m = input().split()
        qtd = 0
        for i in range(int(n), int(m)+1):
            if len(set(list(str(i)))) == len(str(i)):
                qtd += 1
        print(qtd)
                
    except EOFError:
        break
    