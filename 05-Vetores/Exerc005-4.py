# Exercício 005-4:
#
# Faça um programa que faz o seguinte:
#
#   a. lê um número inteiro par N fornecido pelo usuário. O programa deve continuar solicitando o número N enquanto o valor entrado não for par;
#   b. preenche uma lista de tamanho N com números inteiros fornecidos pelo usuário;
#   c. faz a “dobra ao meio” do vetor. Ou seja, você irá criar um vetor com a metade do número de elementos do vetor original, cujas entradas são dadas pela soma dos valores que se encontram quando o vetor é “dobrado ao meio”. Como no exemplo abaixo:
#
# Se o vetor original é dado por v = [4, 5, 8, 9, 3, 7, 6, 1] o vetor resultante da dobra ao meio será v’ = [5, 11, 15, 12] (em que, 5=4+1, 11=5+6, 15=8+7 e 12=9+3).
#
# Exemplos:
#
#   Entrada                 Saída
#   3                       [5, 5]
#   3
#   3
#   1
#   1
#   4
#   1
#   2
#   3
#   4
#   --------------------------------
#   10
#   1                       [11, 10, 10, 11, 4]
#   1
#   1
#   2
#   2
#   2
#   9
#   9
#   9
#   10

print("\n", end="")
lista = []

qtd = 0
while (qtd <= 0 or qtd % 2 != 0):
    while True:
        try:
            qtd = int(input("Quantidade de números à receber: "))
            break
        except ValueError:
            print("Insira um número inteiro.")
    if (qtd <= 0):
        print("Quantidade precisa ser positiva!")
    elif (qtd  % 2 != 0):
        print("Quantidade deve ser par!")

print("\n", end="")
for i in range(qtd):
    lista.append(int(input("Insira um número inteiro: ")))

#Dobra do meio
lista_dobrada = []
for j in range(0, qtd//2):
    lista_dobrada.append(lista[j] + lista[qtd-j-1])
print(f"\nResultado : {lista_dobrada}")
