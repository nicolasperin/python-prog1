# Solicite o nome, a quantidade e o preço de um produto e o percentual de desconto. Exiba o nome do produto, o valor do desconto e o preço a pagar.

nomeProduto = str(input("Insira o nome do produto: "))
quantidadeDeProdutos = int(input("Informe a quantidade de produtos: "))
precoProduto = float(input("Informe agora o preço unitário do produto: "))
percentualDeDesconto = float(input("Informe o percentual de desconto a ser aplicado: "))
valorTotal = quantidadeDeProdutos * precoProduto

valorDesconto = valorTotal * percentualDeDesconto / 100

valorAposDesconto = valorTotal - valorDesconto

print("Nome do produto: %s" %nomeProduto)
print("Desconto total: %.2f" %valorDesconto)
print("Valor final a ser pago: %.2f" %valorAposDesconto)
