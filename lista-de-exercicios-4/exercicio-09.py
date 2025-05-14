questao = 1
aluno = 1
pontuacao = 0
soma_notas = 0

print("PROVA\nDigite a resposta da questão - Use 'A', 'B', 'C', 'D' ou 'E'")
while True:
    while questao <= 10:
        #ler a resposta e validar
        resposta = str(input("Questão %d: " %questao)).upper() 
        while (resposta != "A") and (resposta != "B") and (resposta != "C") and (resposta != "D") and (resposta != "E"):
            resposta = str(input("Resposta inválida!\nQuestão %d: " %questao))

        #incrementar 1 na pontuação caso a resposta estiver correta
        if (questao == 1 and resposta == "A") or (questao == 2 and resposta == "B") or (questao == 3 and resposta == "C") or (questao == 4 and resposta == "D") or (questao == 5 and resposta == "E") or (questao == 6 and resposta == "E") or (questao == 7 and resposta == "D") or (questao == 8 and resposta == "C") or (questao == 9 and resposta == "B") or (questao == 10 and resposta == "A"):
            pontuacao += 1
        
        questao += 1

    if aluno == 1:
        maior_nota = pontuacao
        menor_nota = pontuacao
    else:
        if pontuacao > maior_nota:
            maior_nota = pontuacao
        if pontuacao < menor_nota:
            menor_nota = pontuacao
        

    soma_notas = soma_notas + pontuacao

    continuar = str(input("Outro aluno fará uma prova? (S/N): ")).upper()
    while continuar != "S" and continuar != "N":
        continuar = str(input("Resposta inválida!\nOutro aluno fará uma prova? (S/N): ")).  upper()

    if continuar == "S":
        aluno += 1
        pontuacao = 0
        questao = 1
    else:
        break

media_sala = soma_notas / aluno
print("\nUm total de %d alunos fez a prova" %aluno)
print("A menor nota foi %d" %menor_nota)
print("A maior nota foi %d" %maior_nota)
print("A média de pontuação da turma foi %.2f pontos" %media_sala)

        

        

            