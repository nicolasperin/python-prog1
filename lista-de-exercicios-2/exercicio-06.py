#Exercício 6 - alcool e gasolina 

litros = int(input("Informe a quantidade de litros: "))
tipo_combustivel = str(input("Digite o tipo de combustível desejado. Use A para álcool e use G para gasolina: ")).upper()

if tipo_combustivel == "A":
    if litros > 20:
        litro_com_desconto = 3.2 - (3.2 * 0.05)
    elif litros > 0:
        litro_com_desconto = 3.2 - (3.2 * 0.03)
    else:
        print("Quantidade de litros inválida")
        litro_com_desconto = 0

elif tipo_combustivel == "G":
    if litros > 20:
        litro_com_desconto = 3.9 - (3.9 * 0.06)
    elif litros > 0:
        litro_com_desconto = 3.9 - (3.9 * 0.04)
    else:
        print("Quantidade de litros inválida")
        litro_com_desconto = 0
else:
    print("Tipo de combustível inválido")

valor_total = litros * litro_com_desconto

print("O valor final a ser pago é %.2f" %valor_total)