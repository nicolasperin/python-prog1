def ler_resposta(mensagem):
    while True:
        resposta = input(mensagem).strip().upper()
        if resposta in ['A', 'B', 'C', 'D', 'E']:
            return resposta
        else:
            print("Resposta inválida! Digite apenas A, B, C, D ou E.")

def cadastrar_gabarito():
    print("Cadastro do Gabarito")
    gabarito = []
    i = 0
    while i < 10:
        resposta = ler_resposta(f"Digite o gabarito da questão {i + 1}: ")
        gabarito.append(resposta)
        i += 1
    return gabarito

def aplicar_prova(gabarito):
    print("\nRespostas do Aluno")
    nota = 0
    i = 0
    while i < 10:
        resposta = ler_resposta(f"Resposta da questão {i + 1}: ")
        if resposta == gabarito[i]:
            nota += 1
        i += 1
    print(f"Nota do aluno: {nota}/10")
    return nota

def perguntar_continuar():
    resposta = input("Outro aluno vai utilizar o sistema? (S/N): ").strip().upper()
    while resposta not in ['S', 'N']:
        resposta = input("Digite apenas 'S' para sim ou 'N' para não: ").strip().upper()
    return resposta == 'S'

def mostrar_resultados(total, maior, menor, soma):
    if total == 0:
        print("Nenhum aluno utilizou o sistema.")
        return
    media = soma / total
    print(f"Total de alunos: {total}")
    print(f"Maior nota: {maior}")
    print(f"Menor nota: {menor}")
    print(f"Média da turma: {media:.2f}")

def main():
    gabarito = cadastrar_gabarito()

    total_alunos = 0
    soma_notas = 0
    maior_nota = 0
    menor_nota = 10

    continuar = True
    while continuar:
        nota = aplicar_prova(gabarito)

        if total_alunos == 0:
            menor_nota = nota

        if nota > maior_nota:
            maior_nota = nota
        if nota < menor_nota:
            menor_nota = nota

        total_alunos += 1
        soma_notas += nota

        continuar = perguntar_continuar()

    mostrar_resultados(total_alunos, maior_nota, menor_nota, soma_notas)

main()
