#1146 - Sequências Crescentes

num = int(input())

while num != 0:
    for i in range(1, num+1):
        if i == num:
            print(i)
        else:
            print(i, end=' ')
    num = int(input())
