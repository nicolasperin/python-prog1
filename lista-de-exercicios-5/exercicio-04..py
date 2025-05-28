'''
Faça um programa para imprimir:
 1
 1 2
 1 2 3
 .....
 1 2 3 4 ... n
para um n informado pelo usuário. Use uma função para ler e validar o valor n (inteiro e
positivo) e outra função para imprimir até a n-ésima linha.

'''

def lerN():
    n = int(input("Informe o valor de n: "))
    while n <= 0:
        n = int(input("Valor inválido!\nInforme o valor de n: "))
    return n

def imprimir(n):
    cont = 1
    num_atual = 1
    while cont <= n:
        while num_atual <= cont:
            print(f"{num_atual}", end=" ")    
            num_atual += 1
        print()
        cont += 1
        num_atual = 1

n = lerN()

imprimir(n)