#Exercício 001-5:

#Faça um programa que leia o nome de um vendedor, o seu salário fixo e o total de vendas efetuadas por ele no mês (em dinheiro). Sabendo que este vendedor ganha 5% de comissão sobre suas vendas efetuadas, informar o total a receber no final do mês, com duas casas decimais.


nomeVendedor = (input('\nInsira o nome do vendedor: '))
salarioFixo = float(input('Inisra o salário fixo do vendedor: R$ '))
totalVendas = int(input('Insira o total de vendas efetuadas neste mês pelo vendedor: R$ '))
comissao = 5 / 100

totalReceber = (totalVendas * (comissao)) + salarioFixo
print(f'O salário total a ser recebido por {nomeVendedor} é de R$ {totalReceber:.2f} no final do mês.')