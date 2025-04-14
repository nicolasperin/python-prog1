# Faça um programa que peça a hora atual e mostre uma mensagemna tela de acordo com os intervalos abaixo: 0 <= Hora < 5  “VAI DORMIR ...” 5 <= Hora < 12  “BOM DIA” 12 <= Hora < 18  “BOA TARDE” 18 <= Hora < 24  “BOA NOITE” Outro valor  “HORA INVÁLIDA”

hora_atual = int(input("Digite a hora atual: "))

if (hora_atual >= 0) and (hora_atual < 5):
    msg = "VAI DORMIR..."
elif hora_atual < 12:
    msg = "BOM DIA"
elif hora_atual < 18:
    msg = "BOA TARDE"
elif hora_atual < 24:
    msg = "BOA NOITE"
else:
    msg = "HORA INVÁLIDA"

print(msg)