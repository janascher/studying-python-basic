# Exercício 004-3:
#
# Faça um programa que leia uma string e remova todas as suas vogais. Considere que o usuário digitará apenas palavras (strings) sem acento.
#
# Entrada:
# A entrada contém uma única string, sem acento, que pode ter letras maiúsculas ou minúsculas.
#
# Saída:
# Seu programa deve imprimir na tela a string resultante da exclusão de todas as suas vogais. Se o usuário digitar uma palavra que contém apenas vogais, o programa deve imprimir a string vazia (“”), o que corresponde a uma saída “em branco”.
#
# Exemplos:
#
#       Entrada                 Saída
#       BMW                     BMW
#       ------------------------------------------
#       Pindamonhangaba         Pndmnhngb
#       ------------------------------------------
#       uai                     (não imprime nada)
#       ------------------------------------------

print("\n", end="")
frase = str(input("Insira uma frase: "))

vogal = "aeiou"
resultado = ""

for caractere in frase:
    if caractere not in vogal:
        resultado = resultado + caractere

print(
    f"\nResultado:"
    f"\n{resultado}"
)

