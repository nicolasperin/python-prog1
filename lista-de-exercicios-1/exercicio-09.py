# Escreva um programa que pergunte a quantidade de km percorridos por um carro alugado pelo usuário, assim como a quantidade de dias pelos quais o carro foi alugado. Calcule o preço a pagar, sabendo que o carro custa R$ 60,00 por dia e R$ 0,15 por km rodado. 

quilometrosRodados = float(input("Digite a quantidade de quilômetros percorridos com o carro alugado: "))

diasAlugados = int(input("Informe a quantidade de dias que o carro foi alugado: "))

precoTotal = (60 * diasAlugados) + (0.15 * quilometrosRodados)

print("O preço total a ser pago é: %.2f" %precoTotal)