#Exercício 001-3: 

#A conversão de graus Fahrenheit para Celsius é dada pela expressão:
#C . 1.8 = F - 32
#e a conversão de Kelvin para graus Celsius é dada por
#C = k - 273.15
#Faça um programa que recebe como entrada a temperatura em graus Celsius e realize duas conversões: uma para Fahrenheit e outra para Kelvin.

temperatura = float(input("\nDigite a temperatura em graus Celsius: "))

f = temperatura * 1.8 + 32
k = temperatura + 273.15

print(f"\nA temperatura em Fahrenheit é {f:.2f}")
print(f"A temperatura em Kelvin é {k:.2f}")
