# Exercício 002-1:

# Faça um Programa que peça um valor e mostre na tela se o valor é positivo ou negativo.

print("\n", end="")
a = int(input("Insira um número: "))

if a > 0:
    print("O número é positivo.")
elif a < 0:
    print("O número é negativo.")
else:
    print("O número é zero.")
