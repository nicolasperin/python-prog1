'''
Faça um programa que leia um nome de usuário e a sua senha. A senha não pode ser
igual ao nome do usuário, nem menor que 6 caracteres. Caso ocorra o erro, mostre a
mensagem de erro e volte a pedir as informações. No final imprima o nome e a senha.

'''

def lerUsuario():
    nome = str(input("Digite o nome de usuário: "))
    while len(nome) < 3:
        nome = str(input("Nome inválido!\nDigite o nome do usuário: "))
    return nome

def lerSenha():
    senha = str(input("Digite a senha: "))
    while len(senha) < 6 or senha == usuario:
        senha = str(input("Senha inválida! O tamanho da senha deve ser maior ou igual a 6 caracteres e deve ser diferente do nome do usuário\nDigite a senha: "))
    return senha

usuario = lerUsuario()
senha = lerSenha()

print(f"Usuário: {usuario}")
print(f"Senha: {senha}")