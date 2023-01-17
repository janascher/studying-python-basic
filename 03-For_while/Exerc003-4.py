# Exercício 003-4:
#
# Crie um programa que permita imprimir uma representação de um tabuleiro de xadrez.
#
# Entrada:
# O programa recebe um número inteiro, maior ou igual a 1, que indica a dimensão do tabuleiro.
#
# Saída:
# O programa deve desenhar o tabuleiro com dois caracteres que representam as divisões em cores diferentes conforme exemplos apresentados a seguir. (dica: print(“x”,end=””) não muda de linha)
#
# Exemplos:
#       Entrada         Saída
#       3               oxo
#                       xox
#                       oxo
#       -----------------------------
#       1               o

n = 0

while (n <= 0):
    while True:
        try:
            n = int(input('\nInsira um número: '))
            break
        except ValueError:
            print('\nValor inválido. Insira um número inteiro.')
    if (n <= 0):
        print('\nQuantidade precisa ser positiva!')

print("\n", end="")

for i in range(n): #Linha
    for j in range(n): #Coluna
        if (i + j) % 2 == 0:
            print("o","", end="")
        else:
            print("x","", end="")
    print("\n", end="")


#A expressão if (i + j) % 2 == 0 foi utilizada para descobrir se a soma da linha atual (i) com a coluna atual (j) é par ou ímpar. Se o resultado for 0, significa que a soma é par, caso contrário é ímpar.






