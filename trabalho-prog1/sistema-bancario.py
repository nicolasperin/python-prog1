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

def pegarNumeroDaConta(vetorContas):
    numeroConta = int(input("Digite o número da conta: "))
    while numeroConta < 0 or numeroConta in vetorContas:
        numeroConta = int(input("Número de conta inválido\nDigite o número da conta: "))
    return numeroConta

def pegarSaldo():
    saldo = float(input("Informe o saldo a ser depositado: "))
    while saldo < 0:
        saldo = float(input("Saldo inválido!\nDigite o saldo a ser depositado: "))
    return saldo

def inserir_conta(vetorContas, vetorSaldo):
    conta = pegarNumeroDaConta(vetorContas)
    vetorContas.append(conta)
    vetorSaldo.append(0)

def pesquisar_conta(vetorContas, vetorSaldos):
    
    conta = int(input("Digite o número da conta: "))
    while conta < 0:
        conta = int(input("Número de conta inválido\nDigite o número da conta: "))
    
    for i in range(len(vetorContas)):
        if vetorContas[i] == conta:
            print(f"Conta: {vetorContas[i]}\nSaldo: {vetorSaldos[i]}")
            break
    
    print("A pesquisa não gerou resultado!\n")

def depositar(vetorContas, vetorSaldos):
    conta = pegarNumeroDaConta(vetorContas)
    saldo = pegarSaldo()
    for i in range(len(vetorContas)):
        if vetorContas[i] == conta:
            vetorSaldos[i] = vetorSaldos[i] + saldo

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



        elif op == 5:
            print("\n\nEXCLUIR\n\n")
            # Ler a informação para pesquisar
            # Chamar a função para pesquisar no vetor
            # Excluir a posição pesquisada, se encontrar


        elif op == 6:
            print("\n\nLISTAR\n\n")
            # Listar todos os dados dos vetores


        else:
            print("Opção inválida!")

        input("Pressione <enter> para continuar ...")
    


main()
