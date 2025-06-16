def lerNota():
    nota = int(input("Digite a nota: "))
    while (nota < 0 and nota != -1) or nota > 10:
        nota = int(input("Nota inválida!\nDigite a nota: "))
    return nota

def lerVetorNotas( vetNotas ):
    while True:
        nota = lerNota()
        if nota == -1:
            break
        vetNotas.append( nota )
    return vetNotas

def imprimir( vetor ):
    i = 0
    while i < len(vetor) :
        print("Nota %d = %.1f" %(i, vetor[i]))
        i = i + 1

def calcularMedia(notasAluno):
    return sum(notasAluno)/len(notasAluno)

def main():
    notasAluno = [] 
    lerVetorNotas(notasAluno)
    media = calcularMedia (notasAluno)
    print("Média %2.1f" %media)
    imprimir(notasAluno)
main()