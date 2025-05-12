num1 = int(input("Digite o primeiro número inteiro positivo: "))
while num1 < 0:
    num1 = int(input("Número inválido!\nDigite o primeiro número inteiro positivo: "))
    
num2 = int(input("Digite o segundo número inteiro positivo: "))
while num2 < 0:
    num2 = int(input("Número inválido!\nDigite o segundo número inteiro positivo: "))

divisor = 1
mdc = 1 
menor = num1

if num2 < menor:
    menor = num2

while divisor <= menor:
    if num1 % divisor == 0 and num2 % divisor == 0:
        mdc = divisor
    divisor += 1

print("O máximo divisor comum entre %d e %d é: %d" %(num1, num2, mdc))