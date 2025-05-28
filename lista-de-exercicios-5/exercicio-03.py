'''
Faça um programa para imprimir:
 1
 2 2
 3 3 3
 .....
 n n n n n n ... n
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
    while cont <= n:
        print(f"{cont} " * cont)
        cont += 1

n = lerN()

imprimir(n)
