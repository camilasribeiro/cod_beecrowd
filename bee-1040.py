#1040 - Média 3

N1, N2, N3, N4 = input().split()
N1 = float(N1)
N2 = float(N2)
N3 = float(N3)
N4 = float(N4)

Media = ((N1 * 2) + (N2 * 3) + (N3 * 4) + (N4 * 1))/10
print(f'Media: {Media:.1f}')

if Media >= 7.0:
    print('Aluno aprovado.')
elif Media < 5.0:
    print('Aluno reprovado.')
else:
    print('Aluno em exame.')
    Nota_exame = float(input())
    print(f'Nota do exame: {Nota_exame:.1f}')
    MediaF= (Media + Nota_exame)/2
    if MediaF >= 5.0:
        print('Aluno aprovado.')
    else:
        print('Aluno reprovado.')
    print(f'Media final: {MediaF:.1f}')
    