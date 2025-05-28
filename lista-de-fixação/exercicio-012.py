def lerNumero():
    numero = int(input("Informe o número do consumidor: "))
    while numero < 0:
        numero = int(input("Número inválido!\nInforme o número do consumidor: "))
    return numero

def lerConsumo():
    consumo_mensal = float(input("Informe o consumo do mês (kWh): "))
    while consumo_mensal < 0:
        consumo_mensal = float(input("Número inválido!\nInforme o consumo do mês (kWh): "))
    return consumo_mensal

def lerTipoCliente():
    tipo = int(input("1 - Residencial\n2 - Comercial\n3 - Industrial\nInforme o tipo do cliente: "))
    while tipo != 1 and tipo != 2 and tipo != 3:
        tipo = int(input("Tipo inválido!\n1 - Residencial\n2 - Comercial\n3 - Industrial\nInforme o tipo do cliente: "))             
    return tipo

cont = 1
soma_tipo1, soma_tipo2, soma_tipo3 = 0, 0, 0

while True:
    numero = lerNumero()
    if numero == 0:
        break

    preco_kWh = 0
    
    consumo_mensal = lerConsumo()

    tipo = lerTipoCliente()

    while tipo != 1 and tipo != 2 and tipo != 3:
        tipo = int(input("Tipo inválido!\n1 - Residencial\n2 - Comercial\n3 - Industrial\nInforme o tipo do cliente: "))             
    
    if tipo == 1:
        preco_kWh = 0.3
        soma_tipo1 = soma_tipo1 + (consumo_mensal) 
    elif tipo == 2:
        preco_kWh = 0.5
        soma_tipo2 = soma_tipo2 + (consumo_mensal)
    else:
        preco_kWh = 0.7
        soma_tipo3 = soma_tipo3 + (consumo_mensal)

    print("\nCusto total para esse consumidor:")
    print("R$%.2f\n" %(consumo_mensal * preco_kWh))

if not preco_kWh:
    print("Nenhum consumidor foi informado")
else:
    print("\nOs consumidores de tipo 1 consumiram %.2fkWh " %soma_tipo1)
    print("Os consumidores de tipo 2 consumiram %.2fkWh" %soma_tipo2)
    print("Os consumidores de tipo 3 consumiram %.2fkWh\n" %soma_tipo3)
    print("A média de consumo dos tipos 1 e 2 foi %.2f" %((soma_tipo1 + soma_tipo2)/cont - 1 ))