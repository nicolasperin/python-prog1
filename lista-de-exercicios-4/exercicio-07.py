cont = 1
soma_alturas = 0
soma_pesos = 0

while True:
    codigo = int(input("Digite o código do aluno: "))
    while codigo < 0:
        codigo = int(input("Digite o código do aluno: "))
    
    if codigo == 0:
        break

    altura = float(input("Digite a altura o aluno: "))
    while altura < 0:
        altura = float(input("Digite a altura o aluno: "))
    peso = float(input("Digite o peso do aluno: "))
    while peso < 0:
        peso = float(input("Digite o peso do aluno: "))
    

    if cont == 1:
        maior_altura = altura 
        menor_altura = altura 
        maior_peso = peso 
        menor_peso = peso
        codigo_gordo = codigo 
        codigo_magro = codigo 
        codigo_alto = codigo 
        codigo_baixo = codigo 
    else:
        if altura > maior_altura:
            maior_altura = altura
            codigo_alto = codigo
        if altura < menor_altura:
            menor_altura = altura
            codigo_baixo = codigo
        if peso > maior_peso:
            maior_peso = peso
            codigo_gordo = codigo
        if peso < maior_peso:
            maior_peso = peso
            codigo_magro = codigo
    soma_alturas = soma_alturas + altura
    soma_pesos = soma_pesos + peso

    cont += 1 

if not soma_alturas:
    print("Nenhum aluno informado!")
else:
    media_altura = soma_alturas / cont - 1 
    media_pesos = soma_pesos / cont - 1
    print("\nO código do aluno mais alto é %d e ele mede %.2f m" %(codigo_alto, maior_altura))
    print("O código do aluno mais baixo é %d e ele mede %.2f m" %(codigo_baixo, menor_altura))
    print("O código do aluno mais gordo é %d e ele pesa %.2f kg" %(codigo_gordo, maior_peso))
    print("O código do aluno mais magro é %d e ele pesa %.2f kg" %(codigo_magro, menor_peso))
    print("\n A média de altura dos alunos é %.2f" %media_altura)
    print("A média de peso dos alunos é %.2f\n" %media_pesos)