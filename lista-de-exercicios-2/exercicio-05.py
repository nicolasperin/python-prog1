# Faça um Programa que leia três números e mostre o maior, o menor e mostre‐osemordem decrescente

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o primeiro segundo: "))
num3 = float(input("Digite o primeiro terceiro: "))

if num1 > num2 and num1 > num3:
    maior = num1
    if num2 > num3:
        meio = num2
        menor = num3
    else:
        meio = num3
        menor = num2
elif num2 > num1 and num2 > num3:
    maior = num2
    if num1 > num3:
        meio = num1
        menor = num3
    else:
        meio = num3
        menor = num1
elif num3 > num1 and num3 > num2:
    maior = num3
    if num1 > num2:
        meio = num1
        menor = num2
    else:
        meio = num2
        menor = num1

print("O maior número é: %d\nO menor número é: %d" %(maior,menor))
print("A ordem decrescente dos números informados é: %d, %d, %d" %(maior, meio, menor))
