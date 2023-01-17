# Exercício 001-7:

# Faça um programa que leia um valor inteiro representando um valor em reais e calcule o menor número de cédulas possíveis no qual o valor pode ser decomposto. As cédulas consideradas são as de R$200.00, R$100.00, R$50.00, R$20.00, R$10.00, R$5.00, R$2.00 e R$1.00. Seu programa deve imprimir a quantidade de cada cédula. Dica: divisão inteira usa // e resto da divisão usa % Assim valor total R$ 1317,00 quantas notas de R$ 200,00 qtdNotas200 = valorTotal // 200 resulta 6 notas de 200 e agora o resto seria restoValor = valorTotal % 200 resulta 117

print("\n", end="")
valorTotal = int(input('Digite um valor inteiro: '))

qtdNotas200 = valorTotal // 200
valorResto = valorTotal % 200
qtdNotas100 = valorResto // 100
valorResto = valorResto % 100
qtdNotas50 = valorResto // 50
valorResto = valorResto % 50
qtdNotas20 = valorResto // 20
valorResto = valorResto % 20
qtdNotas10 = valorResto // 10
valorResto = valorResto % 10
qtdNotas5 = valorResto // 5
valorResto = valorResto % 5
qtdNotas2 = valorResto // 2
valorResto = valorResto % 2
qtdNotas1 = valorResto // 1
valorResto = valorResto % 1

print("\n", end="")
print(f'Valor é de..................... R$ {valorTotal}')
print(f'Valor total.................... R$ {valorTotal}')
print("\n", end="")
print(f'Quantidade de notas de 200..... {qtdNotas200}')
print(f'Quantidade de notas de 100..... {qtdNotas100}')
print(f'Quantidade de notas de 50...... {qtdNotas50}')
print(f'Quantidade de notas de 20...... {qtdNotas20}')
print(f'Quantidade de notas de 10...... {qtdNotas10}')
print(f'Quantidade de notas de 5....... {qtdNotas5}')
print(f'Quantidade de notas de 2....... {qtdNotas2}')
print(f'Quantidade de notas de 1....... {qtdNotas1}')
print("\n", end="")
print(f'Resulta........................ {valorResto}')
