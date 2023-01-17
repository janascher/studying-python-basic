# Exercício 002-4:

# Faça um Programa que leia três números usando condicionais e lista-os em ordem decrescente.

print("\n", end="")
n1 = int(input("Insira o primeiro número : "))
n2 = int(input("Insira o segundo número  : "))
n3 = int(input("Insira o terceiro número : "))

if n1 >= n2 and n1 >= n3:
    maior = n1
    if n2 >= n3:
        meio = n2
        menor = n3
    else:
        meio = n3
        menor = n2
elif n2 >= n1 and n2 >= n3:
    maior = n2
    if n1 >= n3:
        meio = n1
        menor = n3
    else:
        meio = n3
        menor = n1
else:
    maior = n3
    if n1 >= n2:
        meio = n1
        menor = n2
    else:
        meio = n2
        menor = n1

print("\nOrdem decrescente : ", maior, meio, menor)
