# Exercício 004-2:
#
# Faça um programa que lê um caractere C (uma string de tamanho 1) e uma string S. O programa deve imprimir a string S com todos os caracteres C (maiúsculos e minúsculos) removidos.
#
# (Dica: Você pode usar o comando str.lower() para converter uma string str para letras minúsculas), (dica 2: não vale usar a função replace).
#
# Exemplos:
#
#       Entrada                                         Saída
#       o                                               lá todos!
#       Olá todos!
#       --------------------------------------------------------
#       e
#       Não faz sentido viver sem poder pedalar.        Não faz sentido viver sem poder pedalar.

print("\n", end="")

letra = str(input("Insira uma letra: ")).lower().strip()
frase = str(input("Insira uma frase: ")).lower().strip()

resultado = ""

for caracter in frase:
    if caracter != letra:
        resultado = resultado + caracter

print(
    f"\nResultado:"
    f"\n{resultado}"
)