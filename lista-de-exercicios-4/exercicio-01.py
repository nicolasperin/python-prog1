numero = int(input("Informe um número inteiro positivo: "))
while numero < 0:
    numero = int(input("Número inválido!\nInforme um número inteiro positivo: "))

fatorial = numero
cont = 1

while cont < numero:
    fatorial = fatorial * (numero - cont)
    cont += 1
print("O fatorial do número informado é %d" %fatorial)