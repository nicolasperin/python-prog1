import random
def gerarNumeroAleatorio(min,max):
    return random.randint(min,max)

def vetorAleatorio(vetor):
    for i in range(20):
        num = gerarNumeroAleatorio(1,100)
        vetor.append(num)
    
def parOuImpar(vetorNumerosAleatorios, vetorPar, vetorImpar):
    for i in vetorNumerosAleatorios:
        if i % 2 == 0:
            vetorPar.append(i)
        else:
            vetorImpar.append(i)

def main():
    vetorNumAleatorio = []
    vetorPar = []
    vetorImpar = []
    vetorAleatorio(vetorNumAleatorio)
    parOuImpar(vetorNumAleatorio, vetorPar, vetorImpar)
    
    print(f"O vetor de números aleatórios contém {len(vetorPar)} números pares e {len(vetorImpar)} números ímpares")
    print(vetorNumAleatorio)
    
main()