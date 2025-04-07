# Faça um programa que calcule o aumento de um salário. Ele deve solicitar o valor do salário e a porcentagem do aumento. Exiba o valor do aumento e do novo salário.

salario = float(input("Digite o valor do salário: "))
porcentagemAumento = float(input("Informe a porcentagem de aumento: "))

aumento = salario * porcentagemAumento / 100
novoSalario = salario + aumento

print("Salário antigo: %.2f" %salario)
print("Aumento a ser acrescido no salário: %.2f" %aumento)
print("Salário após aumento: %.2f" %novoSalario)

