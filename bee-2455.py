#2455 - Gangorra

p1, c1, p2, c2 = input().split()
p1, c1, p2, c2 = int(p1), int(c1), int(p2), int(c2)

if (p1 * c1) == (p2 * c2):
    print('0')
else:
    if (p1 * c1) < (p2 * c2):
        print('1')
    else:
        print('-1')
