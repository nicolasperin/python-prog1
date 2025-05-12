cont = 1
pontuacao = 0
while cont <= 10:
    if cont == 1:
        resposta = str(input("%d: " %cont)).upper()
        while resposta != "A" and resposta != "B" and resposta != "C" and resposta != "D" and resposta != "E":
            resposta = str(input("Digite uma resposta válida!\n%d: " %cont)).upper()

        if resposta == "A":
            pontuacao += 1
        if resposta == "B":
            pontuacao += 1
        if resposta == "C":
            pontuacao += 1
        if resposta == "D":
            pontuacao += 1
        if resposta == "E":
            pontuacao += 1
        if resposta == "E":
            pontuacao += 1
        if resposta == "D":
            pontuacao += 1
        if resposta == "C":
            pontuacao += 1
        if resposta == "B":
            pontuacao += 1
        if resposta == "A":
            pontuacao += 1

    continuar = str(input("Outro aluno vai fazer a prova (S/N)?: ")).upper()
    while continuar != "S" and continuar != "N":
        continuar = str(input("Resposta inválida!\nOutro aluno vai fazer a prova (S/N)?: ")).upper()

    if continuar == "S":
        cont = 1
        pontuacao = 0