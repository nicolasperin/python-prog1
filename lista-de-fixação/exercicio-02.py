'''
Faça um programa que leia e valide as seguintes informações:
Nome: maior que 3 caracteres;
Idade: entre 0 e 150;
Salário: maior que zero;
Sexo: 'f' ou 'm';
Estado Civil: 's', 'c', 'v', 'd'; (maiúsculas e minúsculas)

'''

def lerNome():
    nome = str(input("Digite o nome: "))
    while len(nome) < 3:
        nome = str(input("Nome inválido!\nDigite o nome: "))
    return nome

def lerIdade():
    idade = int(input("Digite a idade: "))
    while 0 > idade < 150:
        idade = int(input("Idade inválida!\nDigite a idade: "))
    return idade

def lerSalario():
    salario = float(input("Digite o salário: "))
    while salario < 0:
        salario = float(input("Salário inválido!\nDigite o salário: "))
    return salario

def lerSexo():
    sexo = str(input("Digite o sexo (F/M): ")).upper()
    while sexo != "F" and sexo != "M":
        sexo = str(input("Sexo inválido!\nDigite o sexo (F/M):")).upper()
    return sexo

def lerEstadoCivil():
    estadoCivil = str(input("Digite o estado civil (s, c, v, d): "))
    while estadoCivil != "s" and estadoCivil != "S" and estadoCivil != "c" and estadoCivil != "C" and estadoCivil != "v" and estadoCivil != "V" and estadoCivil != "d" and estadoCivil != "D":
        estadoCivil = str(input("Estado civil inválido!\nDigite o estado civil (s, c, v, d):")).upper()
    return estadoCivil

nome = lerNome()
idade = lerIdade()
salario = lerSalario()
sexo = lerSexo()
estadoCivil = lerEstadoCivil()

print(f"Nome: {nome}")
print(f"Idade: {idade}")
print(f"Salário: {salario}")
print(f"Sexo: {sexo}")
print(f"Estado Civil: {estadoCivil}")