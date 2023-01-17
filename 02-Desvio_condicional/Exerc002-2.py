# Exercício 002-2:

# Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.

print("\n", end="")
letra = str(input("Insira uma letra: ")).upper().strip()

if letra == "F":
    print("F - Feminino.")
elif letra == "M":
    print("M - Masculino.")
else:
    print("Sexo inválido.")
