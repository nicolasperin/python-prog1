# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra,escrever: F ­ Feminino, M ­ Masculino ou Sexo Inválido.
 
letra = str(input("Digite F ou M: "))

if letra == "F" or letra == "f":
    sexo = "Feminino"
elif letra == "M" or letra == "m":
    sexo = "Masculino"
else:
    sexo = "Sexo inválido!"

print(sexo)