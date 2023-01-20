# Exercício 005-5:
#
# Dado um vetor V de n elementos (suponha que n é ímpar e positivo), o semiparticionado de V é obtido pelas seguintes operações:
#       - se o primeiro elemento de V for maior do que o último elemento V, trocar a posição desses dois elementos;
#       - se o segundo elemento de V for maior do que penúltimo elemento V, trocar a posição desses dois elementos;
#       - se o terceiro elemento de V for maior do que o antepenúltimo elemento de V, trocar a posição desses dois elementos ;
#       - …
#       - assim por diante até que as posições dos elementos vizinhos do elemento do meio sejam trocadas, caso necessário.
#
# Aqui uma representação esquemática das possíveis operações de troca que são realizadas para se obter o semiparticionado de um vetor:
#
#
# Se V contém apenas um elemento, o semiparticionado de V é o próprio V. Faça um programa que:
#       - leia um número inteiro n estritamente positivo ímpar (não precisa fazer validação, isto é, suponha que n é fornecido corretamente);
#       - cria um vetor V e lê n valores inteiros do usuário e armazena-os em V;
#       - transforme V no semiparticionado de V;
#       - imprima o semiparticionado de V.
#
# Entrada: A entrada é um número inteiro n estritamente positivo ímpar , seguidos dos elementos do vetor V.
#
# Saída: Seu programa deve imprimir na tela o particionado do vetor V.
#
# Exemplos:
#
#   Entrada                 Saída
#   1                       [5]
#   5                
#   --------------------------------
#   5                       [1, 2, 3, 4, 5]
#   5                       
#   4
#   3
#   2
#   1

print("\n", end="")

vetor = []

qtd = 0
while (qtd <= 0):
    while True:
        try:
            qtd = int(input("Quantidade de números à receber: "))
            break
        except ValueError:
            print("Insira um número inteiro.")
    if (qtd <= 0):
        print("Quantidade precisa ser positiva!")

print("\n", end="")
for i in range(qtd):
    vetor.append(int(input("Insira um número: ")))

# transforma V no semiparticionado de V
for j in range(0, qtd//2):
    if vetor[j] > vetor[qtd-1-j]:
        vetor[j], vetor[qtd-1-j] = vetor[qtd-1-j], vetor[j]

# imprime o semiparticionado de V
print("\n", end="")
print(vetor)
