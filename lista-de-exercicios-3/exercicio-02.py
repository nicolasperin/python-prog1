nome_aluno = str(input("Informe o nome do aluno: "))
cont = 1
soma_notas = 0
while len(nome_aluno) < 3 or len(nome_aluno) > 50:
    nome_aluno = str(input("Nome inválido!\nInforme o nome do aluno: "))
    
while cont <= 3:
    nota = float(input("Digite um nota de 0 a 10: "))
    while nota < 0 or nota > 10:
        nota = float(input("Nota inválida!\nDigite um nota de 0 a 10: "))
    soma_notas = soma_notas + nota
    cont += 1

media = soma_notas / 3

if media >= 7:
    print("APROVADO!")
elif media < 6:
    print("REPROVADO!")
else:
    print("PROVA FINAL!")

print("Sua média final foi %.2f" %media)