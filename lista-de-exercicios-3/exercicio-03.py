nome_usuario = str(input("Digite o nome de usuário: "))
while len(nome_usuario) < 4:
    nome_usuario = str(input("Nome inválido!\nDigite o nome de usuário: "))
    
senha = str(input("Digite a senha: "))
while len(senha) < 6 or senha == nome_usuario:
    senha = str(input("Senha inválida!\n Digite a senha: "))
    
print("Nome do usuário: %s" %nome_usuario)
print("Senha do usuário: %s" %senha)

