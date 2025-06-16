def lerNome():
    nome = str(input("Digite o nome: "))
    while len(nome) < 3:
        nome = str(input("Nome inválido!\nDigite o nome: "))
    return nome

def lerNumero():
    numero = int(input("Digite o telefone: "))

    return numero

def lerLetra():
    letra = str(input("Digite a letra: "))
    while len(letra) > 1:
        letra = str(input("Letra inválida!\nDigite a letra: "))
    return letra

def lerDados(vetorNomes, vetorTelefones):
    while True:
        nome = lerNome()
        numero = lerNumero()
        if numero < 0:
            numero = 0
            break
        vetorNomes.append(nome)
        vetorTelefones.append(numero)

def imprimirLetra(vetorNomes, vetorTelefones):
    letra = lerLetra()
    cont = 0
    while cont < len(vetorNomes):
        if vetorNomes[cont][0] == letra:
            print(f"Nome: {vetorNomes[cont]}")
            print(f"Telefone: {vetorTelefones[cont]}")
        cont += 1 

def main():
    vetorNomes = []
    vetorTelefones = []

    lerDados(vetorNomes, vetorTelefones)
    imprimirLetra(vetorNomes, vetorTelefones)

main()