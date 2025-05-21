def lerNumero():
    num = int(input("Digite um número inteiro positivo: "))
    while num < 0:
        num = int(input("Número inválido!\nDigite um número inteiro positivo: "))
    return num    

num1 = lerNumero()
    
num2 = lerNumero()


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