#3465 - Cimba

a, b, c = input().split()
a, b, c = int(a), int(b), int(c)

s = (a + b + c) / 2
area = (s* ((s-a) * (s-b) * (s-c))) ** 0.5

print(f'{area:.3f} m2')
