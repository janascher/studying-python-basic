# Exercício 001-6:

# Faça um programa que leia três números inteiros e apresente o maior dos três valores. Nesta questão está proibido usar if (isto é, não deve se usar nenhuma estrutura condicional) ou a função max, mas vai precisar usar a função abs(z) que retorna com o valor do módulo, sem sinal do parâmetro. Dica: A seguinte fórmula permite calcular o maior valor dados os números x e y: Max(x,y) = (x+y)/2 + abs(y-x)/2

x = int(input('\nDigite o primeiro número: '))
y = int(input('Digite o segundo número: '))
z = int(input('Digite o terceiro número: '))

max_xy = (x + y)/2 + abs(y-x)/2
max_xz = (x + z)/2 + abs(z-x)/2
max_yz = (y + z)/2 + abs(y-z)/2

maiorValor = (max_xy + max_xz + max_yz)/3 + abs(max_xy - max_xz)/3 + abs(max_xy - max_yz)/3

print(f'\nO maior valor é {int(maiorValor)}')
