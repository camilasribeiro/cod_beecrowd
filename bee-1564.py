#1564 - Vai Ter Copa?

while True:
    try:
        reclamacoes = int(input())
        
        if 0 <= reclamacoes <= 100:
            if reclamacoes == 0: print('vai ter copa!')
            else: print('vai ter duas!')
        
    except EOFError:
        break
    