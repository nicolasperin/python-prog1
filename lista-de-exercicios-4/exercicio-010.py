questao = 1
aluno = 1
pontuacao = 0
soma_notas = 0

gabarito = 1

print("PROFESSOR - Digite o gabarito da prova")
while gabarito <= 10:
    questao_1 = str(input("Qual o gabarito da questão %d?: " %gabarito)).upper()
    while (questao_1 != "A") and (questao_1 != "B") and (questao_1 != "C") and (questao_1 != "D") and (questao_1 != "E"):
        questao_1 = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %gabarito)).upper()
    gabarito += 1

    questao_2 = str(input("Qual o gabarito da questão %d?: " %gabarito)).upper()
    while (questao_2 != "A") and (questao_2 != "B") and (questao_2 != "C") and (questao_2 != "D") and (questao_2 != "E"):
        questao_2 = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %gabarito)).upper()
    gabarito += 1

    questao_3 = str(input("Qual o gabarito da questão %d?: " %gabarito)).upper()
    while (questao_3 != "A") and (questao_3 != "B") and (questao_3 != "C") and (questao_3 != "D") and (questao_3 != "E"):
        questao_3 = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %gabarito)).upper()    
    gabarito += 1    

    questao_4 = str(input("Qual o gabarito da questão %d?: " %gabarito)).upper()
    while (questao_4 != "A") and (questao_4 != "B") and (questao_4 != "C") and (questao_4 != "D") and (questao_4 != "E"):
        questao_4 = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %gabarito)).upper()
    gabarito += 1
    
    questao_5 = str(input("Qual o gabarito da questão %d?: " %gabarito)).upper()
    while (questao_5 != "A") and (questao_5 != "B") and (questao_5 != "C") and (questao_5 != "D") and (questao_5 != "E"):
        questao_5 = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %gabarito)).upper()
    gabarito += 1
    
    questao_6 = str(input("Qual o gabarito da questão %d?: " %gabarito)).upper()
    while (questao_6 != "A") and (questao_6 != "B") and (questao_6 != "C") and (questao_6 != "D") and (questao_6 != "E"):
        questao_6 = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %gabarito)).upper()
    gabarito += 1
    
    questao_7 = str(input("Qual o gabarito da questão %d?: " %gabarito)).upper()
    while (questao_7 != "A") and (questao_7 != "B") and (questao_7 != "C") and (questao_7 != "D") and (questao_7 != "E"):
        questao_7 = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %gabarito)).upper()
    gabarito += 1
    
    questao_8 = str(input("Qual o gabarito da questão %d?: " %gabarito)).upper()
    while (questao_8 != "A") and (questao_8 != "B") and (questao_8 != "C") and (questao_8 != "D") and (questao_8 != "E"):
        questao_8 = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %gabarito)).upper()
    gabarito += 1
    
    questao_9 = str(input("Qual o gabarito da questão %d?: " %gabarito)).upper()
    while (questao_9 != "A") and (questao_9 != "B") and (questao_9 != "C") and (questao_9 != "D") and (questao_9 != "E"):
        questao_9 = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %gabarito)).upper()
    gabarito += 1

    questao_10 = str(input("Qual o gabarito da questão %d?: " %gabarito)).upper()
    while (questao_10 != "A") and (questao_10 != "B") and (questao_10 != "C") and (questao_10 != "D") and (questao_10 != "E"):
        questao_10 = str(input("Resposta inválida!\nQual o gabarito da questão %d?: " %gabarito)).upper()
    gabarito += 1
    

print("PROVA\nDigite a resposta da questão - Use 'A', 'B', 'C', 'D' ou 'E'")
while True:
    while questao <= 10:
        #ler a resposta e validar
        resposta = str(input("Questão %d: " %questao)).upper() 
        while (resposta != "A") and (resposta != "B") and (resposta != "C") and (resposta != "D") and (resposta != "E"):
            resposta = str(input("Resposta inválida!\nQuestão %d: " %questao))

        #incrementar 1 na pontuação caso a resposta estiver correta
        if (questao == 1 and resposta == questao_1) or (questao == 2 and resposta == questao_2) or (questao == 3 and resposta == questao_3) or (questao == 4 and resposta == questao_4) or (questao == 5 and resposta == questao_5) or (questao == 6 and resposta == questao_6) or (questao == 7 and resposta == questao_7) or (questao == 8 and resposta == questao_8) or (questao == 9 and resposta == questao_9) or (questao == 10 and resposta == questao_10):
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
print("\nUm total de %d alunos fizeram a prova" %aluno)
print("A menor nota foi %d" %menor_nota)
print("A maior nota foi %d" %maior_nota)
print("A média de pontuação da turma foi %.2f pontos\n" %media_sala)

        

        

            