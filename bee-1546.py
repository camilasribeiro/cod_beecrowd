#1546 - Feedback

casos_teste = int(input())

for i in range(casos_teste):
    qnt_feedbacks = int(input())
    for j in range (qnt_feedbacks):
        feedback = int(input())
        if feedback == 1:
            print('Rolien')
        elif feedback == 2:
            print('Naej')
        elif feedback == 3:
            print('Elehcim')
        else:
            print('Odranoel')
            