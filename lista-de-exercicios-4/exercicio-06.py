cont = 2
soma = 0

print("Lojas Tabajara")
valor_produto = float(input("Produto 1: R$"))

while valor_produto < 0:
    valor_produto = float(input("Produto 1: R$"))

while valor_produto != 0:
    valor_produto = float(input("Produto %d: R$" %cont)) 
    while valor_produto < 0:
        valor_produto = float(input("Produto %d: R$" %cont))
    soma = soma + valor_produto
    cont += 1

cont = 1

dinheiro_cliente = float(input("Qual o valor em dinheiro fornecido pelo cliente: "))
while dinheiro_cliente < 0:
    dinheiro_cliente = float(input("Valor inválido!\nQual o valor em dinheiro fornecido pelo cliente: "))

if dinheiro_cliente < soma:
    print("A compra não pode ser finalizada pois o valor fornecido pelo cliente não é suficiente!")

print("Total: R$%.2f" %soma)
print("Dinheiro: R$%.2f" %dinheiro_cliente)
print("Troco: R$%.2f" %(dinheiro_cliente - soma))

