# Converta uma temperatura digitada em Celsius para Fahrenheit. F = 9*C/5 + 32

temperaturaCelsius = float(input("Digite uma temperatura em Celsius: "))

celsiusParaFahrenheit = ((9 * temperaturaCelsius) / 5) + 32

print("A temperatura em informada convertida paras Fahrenheit é igual a %.2f" %celsiusParaFahrenheit)