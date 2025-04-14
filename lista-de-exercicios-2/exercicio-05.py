# Faça um Programa que leia três números e mostre o maior, o menor e mostre‐osemordem decrescente

num1 = float(input("Digite o primeiro número: "))
num2 = float(input("Digite o primeiro segundo: "))
num3 = float(input("Digite o primeiro terceiro: "))

if num1 > num2 and num1 > num3:
    maior = "Primeiro número é maior"
elif num2 > num3:
    maior = "Segundo número é maior"
else:
    maior = "Terceiro número é maior"

print(maior)