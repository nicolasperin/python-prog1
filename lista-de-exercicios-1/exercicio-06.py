#Calcule o tempo de uma viagem de carro. Pergunte a distância a percorrer e a velocidade média esperada para a viagem. 

distancia = float(input("Informe a quantidade de quilômetros a serem percorridos: "))

velocidadeMedia = float(input("Qual a velocidade média esperada para a viagem? (informe em Km/h): "))

tempo = distancia / velocidadeMedia

print("Você conseguirá concluir a viagem em %.2f horas" %tempo)