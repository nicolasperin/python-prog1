primeiro = 0
segundo = 1
cont = 1

num = int(input("Digite um número inteiro positivo: "))
while num < 0:
    num = int(input("Número inválido!\nDigite um número inteiro positivo: "))

print("Os %d primeiros números da sequência de Fibonacci são: " %num)

while cont <= num:
    print(segundo, end=" ")
    proximo = primeiro + segundo
    primeiro = segundo
    segundo = proximo
    cont += 1



