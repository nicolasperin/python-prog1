pop_A, pop_B = 80000, 200000
cont = 1

while pop_A <= pop_B:
    pop_A = pop_A + pop_A * 0.03 
    pop_B = pop_B + pop_B * 0.015 
    cont += 1 

print("Vai demorar %d anos até que a população de A se iguale ou ultrapasse a população de B" %cont)
