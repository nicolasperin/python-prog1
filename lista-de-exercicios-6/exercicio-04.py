def lerNota(vetor):
    nota = int(input("Digite a nota: "))
    while nota < 0 or nota > 10:
        nota = int(input("Nota inválida!\nDigite uma nota: "))
    vetor.append(nota)

def lerNotasAluno(vetor):
    for i in range(3):
        lerNota(vetor)

def media(vetor):
    return sum(vetor)/len(vetor)

def apagarVetor(vetor):
    for item in vetor:
        vetor.pop(item)

        