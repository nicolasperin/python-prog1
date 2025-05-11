cont = 1
soma_altura = 0
menor_altura, maior_altura = 0, 0

while cont <= 3:
    nome = str(input("Informe o seu nome: "))
    while len(nome) < 3:
        nome = str(input("Nome inválido! O nome precisa ter pelo menos 3 caracteres!\nInforme o seu nome: "))
    altura = float(input("Informe sua altura: "))
    while altura < 0 or altura > 3:
        altura = float(input("Altura inválida!\nInforme sua altura: "))
    
    soma_altura = soma_altura + altura

    if cont == 1:
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
    