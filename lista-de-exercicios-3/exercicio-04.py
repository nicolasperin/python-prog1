nome = str(input("Informe o nome: "))
while len(nome) < 3:
    nome = str(input("Nome inválido!\nInforme o nome: "))

idade = int(input("Informe a idade: "))
while idade < 0 or idade > 150:
    idade = int(input("Idade inválida!\nInforme a idade: "))

salario = float(input("Informe o salário: "))
while salario < 0:
    salario = float(input("Salário inválido!\nInforme o salário: "))

sexo = str(input("Informe o sexo: ")).lower()
while sexo != "f" and sexo != "m":
    sexo = str(input("Sexo inválido! Use 'm' ou 'f'\nInforme o sexo: ")).lower()

estado_civil = str(input("Informe o estado civil (s, c, v, d): ")).lower()
while estado_civil != "s" and estado_civil != "c" and estado_civil != "v" and estado_civil != "d":
    estado_civil = str(input("Estado civil inválido! Use 's', 'c', 'v' ou 'd'\nInforme o estado civil (s, c, v, d): ")).lower()

print("Nome: %s" %nome)
print("Idade: %d" %idade)
print("Salário: %.2f" %salario)
print("Sexo: %s" %sexo)
print("Estado civil: %s" %estado_civil)