cont = 1
cont_pares = 0
cont_impares = 0
soma_pares = 0
soma_impares = 0

numero = int(input("Digite um número positivo entre 1 e 1000: "))
while numero < 0:
    numero = int(input("Número inválido! Comece com um número positivo!\nDigite um número positivo entre 1 e 1000: "))
    
while numero != -1:
    numero = int(input("Informe outro número: "))
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
    else:
        cont_impares += 1
        soma_impares = soma_impares + numero
    
    if cont_pares != 0 and cont_impares != 0:
        media_pares = soma_pares/cont_pares
        media_impares = soma_impares/cont_impares
        soma_total = soma_impares + soma_pares

    cont += 1

print("\nO maior número informado foi %d" %maior_numero)
print("Foram informados %d números pares" %cont_pares)
print("Foram informados %d números ímpares" %cont_impares)
print("A média dos números pares informados foi de %.2f" %media_pares)
print("A média dos números ímpares informados foi de %.2f" %media_impares)
print("A soma total de todos números informados foi igual à %d" %soma_total)
