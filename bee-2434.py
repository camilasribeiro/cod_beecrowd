#2434 - Saldo do Vovô

periodo_interesse, saldo_conta = input().split()
periodo_interesse, saldo_conta = int(periodo_interesse), int(saldo_conta)

menor_valor = saldo_conta

for i in range(periodo_interesse):
    valor = int(input())
    if valor > 0:
        saldo_conta += valor
    else:
        saldo_conta -= abs(valor)
        if menor_valor > saldo_conta:
            menor_valor = saldo_conta

print(menor_valor)
