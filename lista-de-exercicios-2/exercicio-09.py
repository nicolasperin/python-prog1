codigo = int(input("Informe o código do produto: "))
quantidade = int(input("Digite a quantidade de produtos: "))


if codigo < 0:
    preco = 0
    print("Código inválido")
elif codigo <= 10:
    preco = 10
elif codigo <= 20:
    preco = 15
elif codigo <= 30:
    preco = 20
elif codigo <= 40:
    preco = 30

valor_total = preco * quantidade

if valor_total > 500:
    desc = 15/100
elif valor_total > 250:
    desc = 10/100
else:
    desc = 5/100

valor_apos_desconto = valor_total - (valor_total * desc)

print("Preço unitário do produto: %.2f" %preco)
print("Valor total da nota: %.2f" %valor_total)
print("Valor descontado (%.0f%%): %.2f" %(desc * 100, valor_total * desc))
print("Valor total após o desconto: %.2f" %valor_apos_desconto)