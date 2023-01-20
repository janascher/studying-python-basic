# Exercício 005-2:
#
# Escreva um programa que receba uma sequência de palavras e as imprima em ordem inversa.
#
# Entrada: A primeira linha da entrada consiste de um número inteiro N representando o número de palavras que serão fornecidas. As próximas N linhas consistem de uma única palavra por linha.
#
# Saída: A saída do seu programa deve consistir de N linhas, onde cada linha consiste de uma única palavra.
#
# Exemplos:
#
#   Entrada                            Saída
#   5                                  LadyBaby
#   ABBA                               Iron
#   ACDC                               Metallica
#   Metallica                          ACDC
#   Iron                               ABBA
#   LadyBaby

print("\n", end="")

vetor = []

qtd = 0
while (qtd <= 0):
    while True:
        try:
            qtd = int(input("Quantidade de palavras à receber: "))
            break
        except ValueError:
            print("Insira um número inteiro.")
    if (qtd <= 0):
        print("Quantidade precisa ser positiva!")

print("\n", end="")

for i in range(qtd):
    texto = (str(input("Insira uma palavra: ")))
    vetor.append(texto)
vetor.reverse()

print("\n", end="")
print(*vetor, sep="\n")
