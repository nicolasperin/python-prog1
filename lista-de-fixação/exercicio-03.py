'''
5. Desenvolver um programa que leia o nome e a altura de 20 pessoas. Este programa
deverá calcular e mostrar:
a) A altura média do grupo;
b) A menor altura do grupo e o nome da pessoa;
c) A maior altura do grupo e o nome da pessoa;

'''

def lerNome():
    nome = str(input("Informe o seu nome: "))
    while len(nome) < 3:
        nome = str(input("Nome inválido! O nome precisa ter pelo menos 3 caracteres!\nInforme o seu nome: "))
    return nome

def lerAltura():
    altura = float(input("Informe sua altura: "))
    while altura < 0 or altura > 3:
        altura = float(input("Altura inválida!\nInforme sua altura: "))
    return altura

cont = 0
soma_altura = 0

while cont < 19:
    nome = lerNome()
    altura = lerAltura()    
    soma_altura = soma_altura + altura

    if cont == 0:
        menor_altura = altura
        maior_altura = altura
        maior_altura_nome = nome
        maior_altura_nome = nome
    else:
        if altura > maior_altura:
            maior_altura = altura
            maior_altura_nome = nome
        if altura < menor_altura:
            menor_altura = altura
            menor_altura_nome = nome
    cont += 1

media = soma_altura/3

print("A média das alturas das pessoas é %.2fm" %media)
print("A menor pessoa se chama %s e mede %.2fm " %(menor_altura_nome, menor_altura))
print("A maior pessoa se chama %s e mede %.2fm " %(maior_altura_nome, maior_altura))
    