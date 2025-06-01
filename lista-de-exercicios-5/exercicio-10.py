'''
Jogo de Craps. Faça um programa que implemente um jogo de Craps. O jogador lança
um par de dados, obtendo a soma entre 2 e 12. Se na primeira jogada você tirar 7 ou 11,
você ganhou. Se você tirar 2, 3 ou 12 na primeira jogada, isto é chamado de "craps" e
você perdeu. Se na primeira jogada você somou 4, 5, 6, 8, 9 ou 10, este é seu "Ponto".
Seu objetivo agora é continuar jogando os dados até tirar este número novamente. Você
perde, no entanto, se tirar um 7 antes de tirar este “Ponto” novamente.
'''

import random

rodada = 1 

def lancarDado():
    return random.randint(1,6)

def jogarDados():
    input("Pressione ENTER para lançar os dados.")
    d1 = lancarDado()
    d2 = lancarDado()
    soma = d1 + d2
    print("Dado 1: %d" %d1)
    print("Dado 2: %d" %d2)
    print("SOMA: %d" %soma)
    print("---------------------")
    return soma

def rodadaCraps(dinheiro):
    print(f"\nVocê tem R$ {dinheiro:.2f}")
    while True:
        aposta = float(input("Digite o valor que deseja apostar: R$ "))
        if 0 < aposta <= dinheiro:
            break
        else:                
            print("Valor de aposta inválido.")
    
    soma = jogarDados()
    
    if soma == 7 or soma == 11:
        print("Você venceu! Tirou 7 ou 11 de primeira")
        return
    elif soma == 2 or soma == 3 or soma == 12:
        print("Você perdeu! Tirou 2, 3 ou 12 de primeira")
    else:
        ponto = soma
        print(f"Seu ponto é {ponto}")
        while True:
            total_dinheiro = 100
            print(f"Você possui R${total_dinheiro}")
            valor_apostado = float(input("Quanto você quer apostar?: "))
            while valor_apostado < 0 or valor_apostado > total_dinheiro:
                valor_apostado = float(input("Valor inválido!\nQuanto você quer apostar?: "))   
            soma = jogarDados()
            if soma == ponto:
                print("Você venceu! Tirou seu ponto novamente!")
                total_dinheiro = total_dinheiro + 2*valor_apostado
                break
            elif soma == 7:
                print("Você perdeu! Tirou 7 antes de tirar seu ponto novamente")
                total_dinheiro = total_dinheiro - valor_apostado
                break
        return total_dinheiro


def jogarCassino():
    print("Bem-vindo ao jogo de Craps - Cassino!")
    dinheiro = 100.0

    while dinheiro > 0:
        dinheiro = rodadaCraps(dinheiro)
        if dinheiro <= 0:
            print("Você perdeu todo o seu dinheiro. Fim de jogo!")
            break
        continuar = input("Deseja jogar novamente? (s/n): ").strip().lower()
        if continuar != 's':
            print(f"Você saiu do jogo com R$ {dinheiro:.2f}. Até logo!")
            break

# Início do jogo
jogarCassino()
