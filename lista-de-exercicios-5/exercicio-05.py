'''
5. O número de combinações possíveis de m elementos em grupos de n elementos (n <=
m) é dada pela fórmula de combinação m!/((m-n)!n!).
Escreva um programa que lê dois inteiros m e n e calcula a combinação de m, n a n. Crie
uma função para calcular o fatorial e chame essa função várias vezes.
'''

def fat(n):
    fat = n
    while fat > 1:
        n = n * (fat - 1)
        fat -= 1
    return n 

def lerNumero():
    numero = int(input("Digite um número: "))
    while numero <= 0:
        numero = int(input("Número inválido!\nDigite um número: "))
    return numero

def combinacao(m,n):
    return fat(m)/(fat(m - n)*fat(n))

m = lerNumero()
n = lerNumero()

combinacao = combinacao(m,n)

print(combinacao)
