def lerNumero():
    num = float(input("Digite um número positivo: "))
    return num

def lerVetorNumero(vetorNumero):
    while True:
        numero = lerNumero()
        if numero < 0:
            break
        vetorNumero.append(numero)

def inverterVetor(vetorNumero):
    return vetorNumero[::-1]

def main():
    vetorNumero = []
    lerVetorNumero(vetorNumero)
    vetorInvertido = inverterVetor(vetorNumero)
    print(f"Vetor original: {vetorNumero}\nVetor invertido: {vetorInvertido}")

main()