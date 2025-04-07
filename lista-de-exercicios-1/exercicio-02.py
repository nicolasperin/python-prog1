#Faça um programa que peça o nome do aluno e suas 4 notas bimestrais e mostre o nome do aluno e a média.

nomeAluno = str(input("Digite o nome do aluno: "))

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))
nota3 = float(input("Digite a terceira nota: "))
nota4 = float(input("Digite a quarta nota: "))

media = nota1 + nota2 + nota3 + nota4 / 4

print("Aluno: ", nomeAluno)
print("Média das notas bimestrais do aluno: ", media)