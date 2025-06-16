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

def craps():
    soma = jogarDados()
    if soma == 7 or soma == 11:
        print("Você venceu! Tirou 7 ou 11 de primeira.")
    elif soma == 2 or soma == 3 or soma == 12:
        print("Você perdeu! Tirou 2, 3 ou 12 de primeira.")
    else:
        ponto = soma
        print(f"Seu ponto é {ponto}. Continue jogando até tirar {ponto} novamente ou 7 para perder.")
        while True:
            soma = jogarDados()
            if soma == ponto:
                print("Você venceu! Tirou seu ponto novamente!")

                break
            elif soma == 7:
                print("Você perdeu! Tirou 7 antes de tirar seu ponto novamente.")

                break

craps()