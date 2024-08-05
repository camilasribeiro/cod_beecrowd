#1548 - Fila do Recreio

def converte(L, tipo):
    for i in range(len(L)):
        L[i] = tipo(L[i])

def nao_mudaram(a, b):
    qtd = 0
    for i in range(len(a)):
        if a[i] == b[i]:
            qtd += 1
    return qtd
    
qtd_casos = int(input())

for i in range(qtd_casos):
    qtd_alunos = int(input())
    alunos = input().split()
    converte(alunos, int)
    ordenados = sorted(alunos, reverse=True)
    print(nao_mudaram(alunos, ordenados))
    