#Escreva um programa que leia a quantidade de dias, horas, minutos e segundos do usuário. Calcule o total em segundos.
dias = int(input("Informe a quantidade de dias: "))
horas = int(input("Digite a quantidade de horas: "))
minutos = int(input("Digite a quantidade de minutos: "))
segundos = int(input("Digite a quantidade de segundos: "))

minutosParaSegundos = minutos * 60
horasParaSegundos = horas * 3600 #1 hora = 3600 segundos -> 60 minutos * 60 segundos
diasParaSegundos = dias * 24 * 3600

total = diasParaSegundos + horasParaSegundos + minutosParaSegundos + segundos
print(total, " segundos")
# print("Quantidade de segundos: ", )