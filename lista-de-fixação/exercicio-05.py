def populacao():
    pop = int(input("Informe a população inicial de A: "))
    while pop < 0:
        pop = int(input("População inválida!\nInforme a população inicial de A: "))
    return pop


def taxa_crescimento():
    taxa = float(input("Informe a taxa de crescimento: "))
    while taxa <= 0 or taxa > 100:
        taxa = float(input("Taxa de crescimento inválida! Use um valor entre 1 e 100! Informe a taxa de crescimento: "))
    return taxa


cont = 1

pop_A = populacao()
pop_B = populacao()

if pop_A >= pop_B:
    print("A população de A já é maior ou igual a população de B")

taxa_A = taxa_crescimento()
taxa_B = taxa_crescimento()
    
taxa_A = taxa_A/100
taxa_B = taxa_B/100

while pop_A <= pop_B:
    pop_A = pop_A + pop_A * taxa_A 
    pop_B = pop_B + pop_B * taxa_B
    cont += 1 

print("\nVai demorar %d anos até que a população de A se iguale ou ultrapasse a população de B\n" %cont)
