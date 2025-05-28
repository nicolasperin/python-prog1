'''
Faça um programa com funções para ler o nome do aluno e suas três notas. Valide a
entrada das notas. Calcule a média final do aluno e imprima: “APROVADO” se a média for
maior ou igual a 7; “REPROVADO” se a média for menor que 6; e “PROVA FINAL” se a
média estiver entre 6 e 7. Imprima também as notas na ordem decrescente. Faça uma
função para cada operação: ler o nome; ler e validar as notas; calcular a média; imprimir a
mensagem e imprimir as notas na ordem decrescente.
'''
def lerNome():
    nome = str(input("Informe o nome do aluno: "))
    while (len(nome) < 3) or (not nome.isalpha()):
        nome = str(input("Nome inválido!\nInforme o nome do aluno: "))

def lerNota():
    nota = int(input("Informe a nota de 0 a 10: "))
    while (nota < 0) or (nota > 10):
        nota = int(input("Nota inválida!\nInforme a nota de 0 a 10"))
    return nota

def calcularMedia(n1, n2, n3):
    media = (n1 + n2 + n3)/3
    return media

def situacaoAluno(media):
    situacao_aluno = "APROVADO"

    if media < 6:
        situacao_aluno = "REPROVADO"
    elif media < 7:
        situacao_aluno = "PROVA FINAL"

    return situacao_aluno
        
def maiorNota(n1,n2,n3):
    maior_nota = 0
    if n1 > n2 and n1 > n3:
        maior_nota = n1    
    elif n2 > n3:
        maior_nota = n2
    else:
        maior_nota = n3
    return maior_nota


def notaDoMeio(n1,n2,n3):
    if n1 > n2 and n1 < n3:
        nota_meio = n1    
    elif n2 > n1 and n2 < n3:
        nota_meio = n2
    elif n3 > n1 and n3 < n2:
        nota_meio = n3
    return nota_meio


def menorNota(n1,n2,n3):
    if n1 < n2 and n1 < n3:
        menor_nota = n1    
    elif n2 < n3:
        menor_nota = n2
    else:
        menor_nota = n3
    return menor_nota 

def exibirNotasOrdenadas(maior_nota, nota_do_meio, menor_nota):
    print(f"{maior_nota}\n{nota_do_meio}\n{menor_nota}")

nome = lerNome()

n1 = lerNota()
n2 = lerNota()
n3 = lerNota()

maior_nota = maiorNota(n1,n2,n3)
nota_do_meio = notaDoMeio(n1,n2,n3)
menor_nota = menorNota(n1,n2,n3)

media = calcularMedia(n1,n2,n3)

situacao_aluno = situacaoAluno(media)

print(f"Aluno: {nome}\nMédia: {media}\nSituação: {situacao_aluno}")

exibirNotasOrdenadas(maior_nota, nota_do_meio, menor_nota)
