# Exercício 005-1:
#
# Desenvolva um programa com as seguintes funcionalidades:
#
#   a. ler e preencher um vetor com N valores inteiros informados pelo usuário. A variável N deve ser lida inicialmente (portanto por usar um comando for para ler os elementos do vetor).
#   b. No vetor lido verificar se há vizinhos consecutivos iguais. Imprimir os índices das posições de todos os vizinhos repetidos (veja os exemplos de entrada e saída).
#
# Entrada: um número inteiro N positivo seguido de N valores inteiros.
# 
# Saída: Índices do vetor com vizinhos contendo o mesmo valor.
#
# Exemplos:
#
#   Entrada                            Saída
#   8                                  Pos 3 e 4
#   1                                  Pos 5 e 6
#   5
#   7
#   8
#   8
#   9
#   9
#   0

print("\n", end="")

qtd = 0
while (qtd <= 0):
    while True:
        try:
            qtd = int(input('Quantidade de números à receber: '))
            break
        except ValueError:
            print('Insira um número inteiro.')
    if (qtd <= 0):
        print('Quantidade precisa ser positiva!')

vetor = []

print("\n", end="")
for i in range(qtd):
    vetor.append(int(input("Insira um número inteiro: ")))

print("\n", end="")
for i in range(qtd - 1):
    if vetor[i] == vetor[i+1]:
        print(f"Posição {i} e {i+1} são vizinhos")

