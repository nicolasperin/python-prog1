'''
Faça um programa que converta da notação de 24 horas para a notação de 12 horas. Por
exemplo, o programa deve converter 14:25 em 2:25 P.M (outro exemplo: 9:45 converte em
9:45 A.M.). A entrada é dada em dois inteiros, um para a hora e outro para os minutos.
Usar função para ler cada número e validar. Criar outra função para fazer a conversão.
Inclua um loop que permita que o usuário repita esse cálculo para novos valores de
entrada todas as vezes que desejar
'''

def lerHoras():
    horas = int(input("Informe as horas: "))
    while horas < 0 or horas > 24:
        horas = int(input("Horas inválidas!\nInforme as horas: "))
    return horas

def lerMinutos():
    minutos = int(input("Informe os minutos: "))
    while minutos < 0 or minutos > 59:
        minutos = int(input("Minutos inválidos!\nInforme os minutos: "))
    return minutos

def converter(horas, minutos):
    if horas > 12:
        horas = horas - 12
        print(f"O horário informado corresponde à {horas}:{minutos} P.M")
    else:
        print(f"O horário informado corresponde à {horas}:{minutos} A.M")

while True: 
    horas = lerHoras()
    minutos = lerMinutos()

    converter(horas,minutos)

    continuar = str(input("\nDeseja converter outro horário?(S/N): ")).upper()
    while continuar != "S" and continuar != "N":
        continuar = str(input("Resposta inválida!\nDeseja converter outro horário?(S/N): "))

    if continuar == "N":
        break


