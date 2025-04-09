# Escreva um programa para calcular a redução do tempo de vida de um fumante. Pergunte a quantidade de cigarros fumados por dia e quantos anos ele já fumou. Considere que um fumante perde 10 minutos de vida a cada cigarro, calcule quantos dias de vida um fumante perderá. Exiba o total de dias. 

cigarrosFumadosPorDia = int(input("Informe a quantidade de cigarros fumados por dia: "))

anosFumando = int(input("A pessoa fuma há quantos anos?: "))

totalCigarros = anosFumando * 365 * cigarrosFumadosPorDia

totalMinutos = totalCigarros * 10

diasPerdidos = totalMinutos / 1440

print("O total de dias perdidos foi %d dias. PARE DE FUMAR" %diasPerdidos)
