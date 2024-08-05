#2381 - Lista de Chamada

qtd_alunos, sorteado = input().split()
qtd_alunos, sorteado = int(qtd_alunos), int(sorteado)
alunos = []
for i in range(qtd_alunos):
    alunos.append(input())
alunos.sort()
print(alunos[sorteado-1])
