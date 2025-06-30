'''
TEMA 4: Sistema bancário
Crie um sistema para gerenciar as contas de um banco. Seu sistema deve
armazenar o número da conta (vetor de inteiros) e o saldo (vetor de números reais) de
cada cliente. Seu sistema deve possuir as seguintes operações:
• Inserir conta: insere o número da conta no vetor e o saldo com ZERO. Não pode
inserir número da conta repetido.
• Pesquisar por conta: pedir um número da conta e pesquisar no vetor, imprimindo a
conta e o saldo.
• Depositar: pedir o número da conta e o valor a depositar. Pesquisar o número da
conta no vetor e somar o saldo com o valor do depósito.
• Maior saldo: pesquisar qual é a conta com o maior saldo e mostrar o número da
conta e o saldo.
• Excluir uma conta: pedir o número da conta, pesquisar no vetor e excluir do vetor.
• Listar: mostrar todas as contas e seu respectivo saldo.
'''


        

def pegarNumeroDaConta():
    numeroConta = int(input("Digite o número da conta: "))
    while numeroConta < 0:
        numeroConta = int(input("Número de conta inválido\nDigite o número da conta: "))
    return numeroConta

def pegarSaldo():
    saldo = float(input("Informe o saldo a ser depositado: "))
    while saldo < 0:
        saldo = float(input("Saldo inválido!\nDigite o saldo a ser depositado: "))
    return saldo

def inserir_conta(vetorContas, vetorSaldo):
    conta = pegarNumeroDaConta()
    if pesquisa(vetorContas, conta) == None:
        vetorContas.append(conta)
        vetorSaldo.append(0)
    else:
        print("Conta já existente!")

def pesquisa(vetorContas, conta): #Retorna o índice da conta no array de contas
    
   # conta = pegarNumeroDaConta()
    for i in range(len(vetorContas)):
        if vetorContas[i] == conta:
            return i
    
    
def depositar(vetorContas, vetorSaldos):
    conta = pegarNumeroDaConta()
    indice = pesquisa(vetorContas, conta)
    if indice == None:
        print("Conta não encontrada!")
    else:
        saldo = pegarSaldo()
        vetorSaldos[indice] = vetorSaldos[indice] + saldo

def imprimir(indice, vetorContas, vetorSaldo):
    print(f"Conta: {vetorContas[indice]}\nSaldo: {vetorSaldo[indice]}\n")


def pesquisar_conta(vetorContas, vetorSaldo):
    conta = pegarNumeroDaConta()
    indice = pesquisa(vetorContas,conta)
    if indice == None:
        print("A pesquisa não gerou resultado!\n")
    else:
        imprimir(indice, vetorContas, vetorSaldo)
        
def maior_saldo(vetorContas, vetorSaldo): #retorna o índice do maior saldo
    maior_saldo = 0
    for i in range(len(vetorSaldo)):
        if vetorSaldo[i] > maior_saldo:
            indice_maior_saldo = i
            maior_saldo = vetorSaldo[i]
    imprimir(indice_maior_saldo, vetorContas, vetorSaldo)

def excluir(vetorContas, vetorSaldo):
    conta = pegarNumeroDaConta()
    indice = pesquisa(vetorContas,conta)
    if indice == None:
        print("Conta não encontrada!")
    else:
        print("Conta excluída:")
        imprimir(indice, vetorContas, vetorSaldo)
        vetorContas.pop(indice)
        vetorSaldo.pop(indice)

def listar_contas(vetorContas, vetorSaldo):
    for i in range(len(vetorContas)):
        imprimir(i, vetorContas, vetorSaldo)

def menu() :
    op = ""
    while op.isdigit() == False or int(op) < 0 or int(op) > 6:

        print("\n" * 130)        
        print("NOME DO SEU SISTEMA: Sistema Bancário")
        print("1-Inserir conta")
        print("2-Pesquisar por conta")
        print("3-Depositar")
        print("4-Maior saldo")
        print("5-Excluir conta")
        print("6-Listar")
        print("0-Sair")
        op = input("Escolha sua opção: ")
    return int(op)

    
###### PRINCIPAL ##########
def main():
    op = 1
    vetorContas = []
    vetorSaldos = []
    while op != 0:
        op = menu()
        
        if op == 0:
            print("\n\nFim do programa!!!\n\n")
            
        elif op == 1:
            print("\n\nINSERIR\n\n")
            inserir_conta(vetorContas, vetorSaldos)

        elif op == 2:
            print("\n\nPESQUISAR\n\n")
            pesquisar_conta(vetorContas,vetorSaldos)

        elif op == 3:
            print("\n\nATUALIZAR\n\n")
            depositar(vetorContas, vetorSaldos)

        elif op == 4:
            print("\n\nMAIOR\n\n")
            # Chamar a função para pesquisar no vetor o maior elemento
            maior_saldo(vetorContas, vetorSaldos)

        elif op == 5:
            print("\n\nEXCLUIR\n\n")
            # Ler a informação para pesquisar
            # Chamar a função para pesquisar no vetor
            # Excluir a posição pesquisada, se encontrar
            excluir(vetorContas, vetorSaldos)


        elif op == 6:
            print("\n\nLISTAR\n\n")
            # Listar todos os dados dos vetores
            listar_contas(vetorContas, vetorSaldos)

        else:
            print("Opção inválida!")

        input("\n\nPressione <enter> para continuar ...")
    


main()