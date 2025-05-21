def populacao_A():
    pop_A = int(input("Informe a população inicial de A: "))
    while pop_A < 0:
        pop_A = int(input("População inválida!\nInforme a população inicial de A: "))
    return pop_A

def populacao_B():
    pop_B = int(input("Informe a população inicial de B: "))
    while pop_B < 0:
        pop_B = int(input("População inválida!\n Informe a população inicial de B: "))
    return pop_B

def taxa_crescimento_A():
    taxa_A = float(input("Informe a taxa de crescimento de A: "))
    while taxa_A <= 0 or taxa_A > 100:
        taxa_A = float(input("Taxa de crescimento inválida! Use um valor entre 1 e 100! Informe a taxa de crescimento de A: "))
    return taxa_A

def taxa_crescimento_B():
    taxa_B = float(input("Informe a taxa de crescimento de B: "))
    while taxa_B <= 0 or taxa_B > 100:
        taxa_B = float(input("Taxa de crescimento inválida! Use um valor entre 1 e 100! Informe a taxa de crescimento de B: "))
    return taxa_B
        
cont = 1

pop_A = populacao_A()
pop_B = populacao_B()

if pop_A >= pop_B:
    print("A população de A já é maior ou igual a população de B")

taxa_A = taxa_crescimento_A()
taxa_B = taxa_crescimento_B()
    
taxa_A = taxa_A/100
taxa_B = taxa_B/100

while pop_A <= pop_B:
    pop_A = pop_A + pop_A * taxa_A 
    pop_B = pop_B + pop_B * taxa_B
    cont += 1 

print("\nVai demorar %d anos até que a população de A se iguale ou ultrapasse a população de B\n" %cont)
