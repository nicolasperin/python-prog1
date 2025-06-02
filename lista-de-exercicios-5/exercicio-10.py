import random

def lancarDado():
    return random.randint(1, 6)

def jogarDados():
    input("Pressione ENTER para lançar os dados.")
    d1 = lancarDado()
    d2 = lancarDado()
    soma = d1 + d2
    print(f"Dado 1: {d1}")
    print(f"Dado 2: {d2}")
    print(f"SOMA: {soma}")
    print("---------------------")
    return soma

def craps(saldo, aposta):
    soma = jogarDados()
    if soma == 7 or soma == 11:
        print("Você venceu! Tirou 7 ou 11 de primeira.")
        saldo += aposta  # ganha o valor da aposta (dobro do que apostou)
    elif soma == 2 or soma == 3 or soma == 12:
        print("Você perdeu! Tirou 2, 3 ou 12 de primeira.")
        saldo -= aposta
    else:
        ponto = soma
        print(f"Seu ponto é {ponto}. Continue jogando até tirar {ponto} novamente ou 7 para perder.")
        while True:
            soma = jogarDados()
            if soma == ponto:
                print("Você venceu! Tirou seu ponto novamente!")
                saldo += aposta
                break
            elif soma == 7:
                print("Você perdeu! Tirou 7 antes de tirar seu ponto novamente.")
                saldo -= aposta
                break
    return saldo

def cassino():
    saldo = 100.00
    print("Bem-vindo ao Cassino Craps!")
    while saldo > 0:
        print(f"\nSeu saldo atual é: R$ {saldo:.2f}")
        while True:
            aposta = float(input("Quanto deseja apostar? R$ "))
            if aposta <= 0:
                print("A aposta deve ser maior que zero.")
            elif aposta > saldo:
                print("Você não pode apostar mais do que tem.")
            else:
                break

        saldo = craps(saldo, aposta)
        print(f"Saldo atual: R$ {saldo:.2f}")
        
        if saldo <= 0:
            print("Você ficou sem dinheiro. Fim de jogo!")
            break
        
        continuar = input("Deseja continuar jogando? (S/N): ").upper()
        if continuar != 'S':
            print("Obrigado por jogar! Volte sempre.")
            break

cassino()
