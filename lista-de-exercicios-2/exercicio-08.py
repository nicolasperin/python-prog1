# Em uma competição de ginástica, cada atleta recebe votos de cinco jurados. As notassãode 0 a 10. A melhor e a pior nota são eliminadas. A sua nota fica sendo a média dos votos restantes. Você deve fazer um programa que receba o nome do ginasta e as notasdoscinco jurados alcançadas pelo atleta em sua apresentação e depois informe asuamédia,conforme a descrição acima informada (retirar a melhor e a pior nota e depois calcular a média com as notas restantes). As notas não são informadas ordenadas. Ao final mostrar o nome do atleta, sua média, a maior e a menor nota.

nome = str(input("Informe o nome da atleta: "))
nota1 = int(input("Digite uma nota de 0 a 10: "))
nota2 = int(input("Digite uma nota de 0 a 10: "))

if (nota1 > nota2):
    maiorNota = nota1
    menorNota = nota2
else:
    maiorNota = nota2
    menorNota = nota1

nota3 = int(input("Digite uma nota de 0 a 10: "))

if maiorNota < nota3:
    maiorNota = nota3
elif nota3 < menorNota:
    menorNota = nota3

nota4 = int(input("Digite uma nota de 0 a 10: "))

if maiorNota < nota4:
    maiorNota = nota4
elif nota4 < menorNota:
    menorNota = nota4

nota5 = int(input("Digite uma nota de 0 a 10: "))

if maiorNota < nota5:
    maiorNota = nota5
elif nota5 < menorNota:
    menorNota = nota5

media = (nota1 + nota2 + nota3 + nota4 + nota5 - maiorNota - menorNota)/3

print("\nNome do atleta: %s\nMédia do atleta: %.2f\nMaior nota: %d\nMenor nota: %d" %(nome, media, maiorNota, menorNota) )