# Exercício 003-3:
#
# Crie um programa que permita verificar se um número N é fatorial ou não. N é fatorial caso exista um número X >= 0 tal que N = X!.
#
# Entrada:
# O programa recebe um número inteiro N maior ou igual a zero.
#
# Saída:
# O programa deve imprimir Verdadeiro se N é fatorial, caso contrário deve imprimir Falso.
#
# Exemplos:
#
# Entrada N e Saída (Verdadeiro ou Falso), não precisa imprimir na mesma linha.
#
#       1................. Verdadeiro
#       2................. Verdadeiro
#       3................. Falso
#       6................. Verdadeiro
#       12................ Falso
#       24................ Verdadeiro
#       7777.............. Falso
#       1307674368000..... Verdadeiro
#       943675496......... Falso

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

i = 1
fatorial = 1

while fatorial < n:
    i = i + 1
    fatorial = fatorial * i

if fatorial == n:
    print(f'O número {n} é fatorial? Verdadeiro.')
else:
    print(f'O número {n} é fatorial? Falso.')

#Utilizando o "while", o código irá multiplicar "i" pela "fatorial" até que "fatorial" seja maior ou igual a "n". Se no final "fatorial" for igual a "n", o programa imprimirá "Verdadeiro", caso contrário, imprimirá "Falso".