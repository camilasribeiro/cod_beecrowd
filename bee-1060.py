#1060 - Números Positivo

a = 0
p = 0

while a < 6:
    x = float(input())
    a+= 1
    if x != 0:
        if x > 0:
            p += 1

print((p),'valores positivos')
