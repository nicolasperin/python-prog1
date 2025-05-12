soma = 0
numero = int(input("Digite um número inteiro positivo: "))
while numero < 0:
    numero = int(input("Número inválido! Digite um número inteiro positivo: "))
print()
cont = numero

while cont > 0:
    if numero % cont == 0:
        soma = soma + cont
        print("O número é divisível por %d" %cont)
    cont -= 1
    
if soma == numero + 1:
    print("\nO número informado é um número primo\n")
else:
    print("\nO número informado não é um número primo\n")