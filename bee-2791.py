#2791 - Feijão

c1, c2, c3, c4 = input().split()
c1, c2, c3, c4 = int(c1), int(c2), int(c3), int(c4)

lista = c1, c2, c3, c4

pos = 0

for i in lista:
    pos += 1
    if i == 1:
        print(pos)
