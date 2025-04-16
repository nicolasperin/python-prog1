# Faça um programa para uma loja de tintas. O programa deverá pedir o tamanho em metrosquadrados da área a ser pintada. Considere que a cobertura da tinta é de 1 litroparacada3 metros quadrados e que a tinta é vendida em latas de 18 litros, que custam R$80,00. Informe ao usuário a quantidades de latas de tinta a serem compradas e o preço total.Obs. : somente são vendidos um número inteiro de latas

import math

area = float(input("Informe a área a ser pintada (EM METROS): "))

if area < 0:
    litros_necessarios = 0
    print("Área inválida")

litros_necessarios = area / 3
latas = litros_necessarios / 18
latas = math.ceil(latas)

valor_total = latas * 80

print("Você vai precisar de %d latas, isso vai lhe custar R$%.2f" %(latas, valor_total))