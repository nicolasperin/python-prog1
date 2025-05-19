'''
6. Faça um programa para ler vários números positivos entre 1 e 1000, validar e só parar
quando o usuário digitar -1. No final imprima o maior número, a quantidade de números
pares e a quantidade de números ímpares, a média dos números pares e a média dos
números ímpares e a soma total de todos os números lidos.
'''

def lerNumero():
    numero = int(input("Digite um número positivo entre 1 e 1000: "))
    while numero < 0:
        numero = int(input("Número inválido! Comece com um número positivo!\nDigite um número positivo entre 1 e 1000: "))
    return numero

def lerNumerosSeguintes():
    numero = int(input("Digite um número positivo entre 1 e 1000: "))
    return numero


cont = 1
cont_pares = 0
cont_impares = 0
soma_pares = 0
soma_impares = 0
media_pares, media_impares = 0, 0

numero = lerNumero()

while numero != -1:
    numero = lerNumerosSeguintes()
    while numero < 0 and numero != -1:
        numero = int(input("Número inválido! Digite um número positivo!\n Digite um número inteiro entre 1 e 1000: "))
    if cont == 1:
        maior_numero = numero
        menor_numero = numero
    else:
        if numero > maior_numero and numero != -1:
            maior_numero = numero
        if numero < menor_numero and numero != -1:
            menor_numero = numero
    if numero % 2 == 0:
        cont_pares += 1
        soma_pares = soma_pares + numero
        media_pares = soma_pares/cont_pares
    else:
        cont_impares += 1
        soma_impares = soma_impares + numero
        media_impares = soma_impares/cont_impares
    
    if cont_pares != 0 or cont_impares != 0:
        soma_total = soma_impares + soma_pares

    cont += 1

print("\nO maior número informado foi %d" %maior_numero)
print("Foram informados %d números pares" %cont_pares)
print("Foram informados %d números ímpares" %cont_impares)
print("A média dos números pares informados foi de %.2f" %media_pares)
print("A média dos números ímpares informados foi de %.2f" %media_impares)
print("A soma total de todos números informados foi igual à %d" %soma_total)
