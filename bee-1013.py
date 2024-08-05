#1013 - O Maior

a, b, c = input().split()
a = int(a)
b = int(b)
c = int(c)
mab= (a + b + abs(a-b)) / 2
mabc= (mab + c + abs(mab-c)) / 2
print(f'{mabc:.0f} eh o maior')
