# Exercício 003-1:
#
# Desenvolva um programa que simule o funcionamento de uma máquina de somar.
#
# Entrada:
# O seu programa receberá um número inteiro não negativo N que denota a quantidade de números que seu programa receberá para computar o valor total da soma. Na sequência seu programa receberá N números reais.
#
# Saída:
# O seu programa deve imprimir a frase “Total: ” seguida do valor da soma (com duas casas decimais de precisão).
#
# Exemplos:
#
#       Entrada         Saída
#       3               Total: 10.75
#       7.00
#       1.50
#       2.25
#       -----------------------------
#       5               Total: 22.50
#       1.25
#       5.70
#       2.56
#       9.99
#       3.00

qtd = 0
while (qtd <= 0):
    while True:
        try:
            qtd = int(input('\nQuantidade de números à receber: '))
            break
        except ValueError:
            print('\nValor inválido. Insira um número inteiro.')
    if (qtd <= 0):
        print('\nQuantidade precisa ser positiva!')

soma = 0
for i in range(0, qtd):
    num = float(input('Insira um número: '))
    soma = soma + num
print (f'Soma dos números: {soma:.2f}')
