'''
Faça um programa que use a função valorPagamento para determinar o valor a ser pago
por uma prestação de uma conta. O programa deverá solicitar ao usuário o valor da
prestação e o número de dias em atraso e passar estes valores para a função
valorPagamento, que calculará o valor a ser pago e devolverá este valor ao programa que
a chamou. O programa deverá então exibir o valor a ser pago na tela. Após a execução o
programa deverá voltar a pedir outro valor de prestação e assim continuar até que seja
informado um valor igual a zero para a prestação. Neste momento o programa deverá ser
encerrado, exibindo o relatório do dia, que conterá a quantidade e o valor total de
prestações pagas no dia. O cálculo do valor a ser pago é feito da seguinte forma. Para
pagamentos sem atraso, cobrar o valor da prestação. Quando houver atraso, cobrar 3% de
multa, mais 0,1% de juros por dia de atraso.
'''

def valorPrestacao():
    valor_prestacao = float(input("Informe o valor da prestação: "))
    while valor_prestacao < 0:
        valor_prestacao = float(input("Valor inválido!\nInforme o valor da prestação: "))
    return valor_prestacao

def diasAtraso():
    dias_atraso = int(input("Informe a quantidade de dias de atraso no pagamento da prestação: "))
    while dias_atraso < 0:
        dias_atraso = int(input("Valor inválido!\nInforme a quantidade de dias de atraso no pagamento da prestação: "))
    return dias_atraso

def valorPagamento(valor_prestacao, dias_atraso):
    if dias_atraso > 0:
        valor_pagamento = (valor_prestacao * 1.03)
        valor_pagamento = (valor_pagamento + (0.001 * dias_atraso) * valor_pagamento)
    else:
        valor_pagamento = valor_prestacao
    return valor_pagamento

qtd_prestacoes = 0
soma_valores_prestacoes = 0

while True:
    valor_prestacao = valorPrestacao()
    dias_atraso = diasAtraso()

    if valor_prestacao == 0:
        break   

    valor_pagamento = valorPagamento(valor_prestacao, dias_atraso)
    qtd_prestacoes += 1
    soma_valores_prestacoes = soma_valores_prestacoes + valor_pagamento
    print(f"Valor a ser pago por essa prestação: R${valor_pagamento}\n")

print(f"\nHoje foram pagas {qtd_prestacoes} prestações")
print(f"O valor total pago por essas prestações foi de R${soma_valores_prestacoes:.2f}")