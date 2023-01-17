#Exercício 001-4:

#Leia dois números inteiros a, b, e dois números em ponto flutuante x, y. Então calcule a expressão: a + bx – sqrt(b) + ( (a+b) / (x-y) ) atribuindo o resultado à variável expressão. A seguir, mostre a variável expressão com a mensagem correspondente, conforme exemplos abaixo. A saída deve imprimir duas casas decimais.

import math

a = int(input('\nInsira um valor inteiro de a: '))
b = int(input('Insira um valor inteiro de b: '))
x = float(input('Insira um valor com duas casas decimais de x: '))
y = float(input('Insira um valor com duas casas decimais de y: '))

expressao = a + (b * x) - math.sqrt(b) + ((a+b) / (x - y))
print(f'A expressão é: {expressao:.2f}')