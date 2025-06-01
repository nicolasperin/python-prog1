'''
Altere o exercício 10 da Lista 4 para usar funções. Será necessário apenas uma função
para ler e validar a resposta (“A”, “B”, “C”, “D”, “E”). Essa função será chamada 10 vezes,
uma vez para cada questão, para preencher o gabarito e depois será chamada mais 10
vezes para ler as respostas dos alunos
'''


def lerGabarito(num_questao):
    gabarito = str(input("Qual o gabarito da questão %d?: " %num_questao)).upper()
    while (gabarito != "A") and (gabarito != "B") and (gabarito != "C") and (gabarito != "D") and (gabarito != "E"):
        gabarito = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %num_questao)).upper()
    return gabarito

num_questao = 1
aluno = 1
pontuacao = 0
soma_notas = 0
questao = 1

print("PROFESSOR - Digite o gabarito da prova")

gab_questao_1 = lerGabarito(num_questao)
num_questao += 1
gab_questao_2 = lerGabarito(num_questao)
num_questao += 1
gab_questao_3 = lerGabarito(num_questao)
num_questao += 1
gab_questao_4 = lerGabarito(num_questao)
num_questao += 1
gab_questao_5 = lerGabarito(num_questao)
num_questao += 1
gab_questao_6 = lerGabarito(num_questao)
num_questao += 1
gab_questao_7 = lerGabarito(num_questao)
num_questao += 1
gab_questao_8 = lerGabarito(num_questao)
num_questao += 1
gab_questao_9 = lerGabarito(num_questao)
num_questao += 1
gab_questao_10 = lerGabarito(num_questao)

num_questao = 1

print("PROVA\nDigite a resposta da questão - Use 'A', 'B', 'C', 'D' ou 'E'")

questao_1 = lerGabarito(num_questao)
num_questao += 1
questao_2 = lerGabarito(num_questao)
num_questao += 1
questao_3 = lerGabarito(num_questao)
num_questao += 1
questao_4 = lerGabarito(num_questao)
num_questao += 1
questao_5 = lerGabarito(num_questao)
num_questao += 1
questao_6 = lerGabarito(num_questao)
num_questao += 1
questao_7 = lerGabarito(num_questao)
num_questao += 1
questao_8 = lerGabarito(num_questao)
num_questao += 1
questao_9 = lerGabarito(num_questao)
num_questao += 1
questao_10 = lerGabarito(num_questao)
num_questao += 1

num_questao = 1
while True:
    while num_questao <= 10:
        if (num_questao == 1 and gab_questao_1 == questao_1) or (num_questao == 2 and gab_questao_2 == questao_2) or (num_questao == 3 and gab_questao_3 == questao_3) or (num_questao == 4 and gab_questao_4 == questao_4) or (num_questao == 5 and gab_questao_5 == questao_5) or (num_questao == 6 and gab_questao_6 == questao_6) or (num_questao == 7 and gab_questao_7 == questao_7) or (num_questao == 8 and gab_questao_8 == questao_8) or (num_questao == 9 and gab_questao_9 == questao_9) or (num_questao == 10 and gab_questao_10 == questao_10):
            pontuacao += 1

        num_questao += 1

    num_questao = 1

    if aluno == 1:
        maior_nota = pontuacao
        menor_nota = pontuacao
    else:
        if pontuacao > maior_nota:
            maior_nota = pontuacao
        if pontuacao < menor_nota:
            menor_nota = pontuacao
        

    soma_notas = soma_notas + pontuacao
    print (num_questao)

    continuar = str(input("Outro aluno fará uma prova? (S/N): ")).upper()
    while continuar != "S" and continuar != "N":
        continuar = str(input("Resposta inválida!\nOutro aluno fará uma prova? (S/N): ")).upper()

    if continuar == "S":
        aluno += 1
        pontuacao = 0
        num_questao = 1
    else:
        break

media_sala = soma_notas / aluno
print("\nUm total de %d alunos fizeram a prova" %aluno)
print("A menor nota foi %d" %menor_nota)
print("A maior nota foi %d" %maior_nota)
print("A média de pontuação da turma foi %.2f pontos\n" %media_sala)

        

        