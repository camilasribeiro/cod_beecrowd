#1097 - Sequencia IJ 3

i = 1
j = 7
c = 0

while c <= 4:
    print(f'I={i} J={j}')
    print(f'I={i} J={j-1}')
    print(f'I={i} J={j-2}')   
    i += 2
    j += 2
    c += 1
    