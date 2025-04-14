# Faça um programa para a leitura de duas notas parciais de um aluno. O programa deve calcular a média alcançada por aluno e apresentar a mensagem: ­ "Aprovado", se a média alcançada for maior ou igual a sete; ­ "Reprovado", se a média for menor do que sete; ­ "Aprovado com Distinção", se a média for igual a dez.

nota1 = float(input("Digite a primeira nota: "))
nota2 = float(input("Digite a segunda nota: "))

media = (nota1 + nota2) / 2

if media == 10:
    situacao = "Aprovado com Distinção"
elif media >= 7:
    situacao = "Aprovado"
else: 
    situacao = "Reprovado"

print(situacao)