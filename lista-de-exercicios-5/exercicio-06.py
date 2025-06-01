'''
Faça um programa com uma função chamada somaImposto. A função possui dois
parâmetros formais: taxaImposto, que é a quantia de imposto sobre vendas expressa em
porcentagem; e valorCusto, que é o custo de um item antes do imposto. A função retorna
o valor de custo acrescentado com o imposto sobre vendas.
'''

def lerValorCusto():
    valor_custo = float(input("Informe o valor de custo: "))
    while valor_custo <= 0:
        valor_custo = float(input("Valor inválido!\nInforme o valor de custo: "))
    return valor_custo

def lerTaxaImposto():
    taxa_imposto = float(input("Informe a quantia de imposto em (0-100)%: "))
    while taxa_imposto < 0:
        taxa_imposto = float(input("Valor inválido!\nInforme a quantia de imposto em (0-100)%: "))
    return taxa_imposto

def somaImposto(valor_custo, taxa_imposto):
    imposto_porc = taxa_imposto / 100
    valor_apos_imposto = valor_custo + (valor_custo * imposto_porc)
    return valor_apos_imposto


valor = lerValorCusto()
imposto = lerTaxaImposto()

valor_com_imposto = somaImposto(valor, imposto)
print(f"O valor de custo após a aplicação de imposto é de R${valor_com_imposto}")