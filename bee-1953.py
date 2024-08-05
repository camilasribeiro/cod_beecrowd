#1953 - Roberto e a Sala Desenfreada

while True:
    try:
        qtd_alunos = int(input())
        a = 1
        epr = 0
        ehd = 0
        intrusos = 0
        
        while a <= qtd_alunos :
            m, s = input().split()
            m = int(m)
            if s == 'EPR' or s == 'epr':
                epr += 1
            elif s == 'EHD' or s == 'ehd':
                ehd += 1
            else:
                intrusos += 1
            a+= 1
        
        print('EPR:', epr)
        print('EHD:', ehd)
        print('INTRUSOS:', intrusos)
        
    except EOFError:
        break
    