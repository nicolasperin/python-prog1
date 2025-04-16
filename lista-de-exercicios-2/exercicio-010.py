idade = int(input("Informe a idade do paciente: "))
peso = int(input("Informe o peso do paciente em quilos: "))

if idade >= 12:
    if peso >= 60:
        dosagem = 1000
    else:
        dosagem = 875
else:
    if peso > 30:
        dosagem = 750
    elif peso > 24:
        dosagem = 500
    elif peso > 16:
        dosagem = 375
    elif peso > 9:
        dosagem = 250
    elif peso >= 5:
        dosagem = 125
    else:
        dosagem = 0

# Uma gota = 25mg 

gotas_necessarias = dosagem / 25

print("O paciente vai precisar de %d gotas" %gotas_necessarias)


