# Exercício 002-6:

# Faça um programa para o cálculo de uma folha de pagamento, sabendo que os descontos são do Imposto de Renda, que depende do salário bruto (conforme tabela abaixo) e 3% para o Sindicato e que o FGTS corresponde a 11% do Salário Bruto, mas não é descontado (é a empresa que deposita). O Salário Líquido corresponde ao Salário Bruto menos os descontos. O programa deverá pedir ao usuário o valor da sua hora e a quantidade de horas trabalhadas no mês.
#
# Desconto do IR:
#   Salário Bruto até 900 (inclusive)  - isento
#   Salário Bruto até 1500 (inclusive) - desconto de 5%
#   Salário Bruto até 2500 (inclusive) - desconto de 10%
#   Salário Bruto acima de 2500        - desconto de 20%
#
#Imprima na tela as informações, dispostas conforme o exemplo abaixo. No exemplo o valor da hora é 5 e a quantidade de hora é 220.
#
#   Salário Bruto         : (5 * 220)  : R$ 1100,00 
#   (-) IR (5%)           : R$ 55,00 
#   (-) INSS ( 10%)       : R$ 110,00 
#   FGTS (11%)            : R$ 121,00 
#   Total de descontos    : R$ 165,00 
#   Salário Liquido       : R$ 935,00

print("\n", end="")
valorHora = float(input("Informe o valor da sua hora: R$ "))
qtdTrabalhadas = float(input("Informe a quantidade de horas trabalhadas no mês: "))

salarioBruto = float((valorHora * qtdTrabalhadas))

# Desconto IR
if salarioBruto <= 900:
    # desconto de 0%
    descontoIR = 0
    descIR = salarioBruto * descontoIR
    salarioDesc = salarioBruto - descIR
elif salarioBruto <= 1500:
    # desconto de 5%
    descontoIR = 0.05
    descIR = salarioBruto * descontoIR
    salarioDesc = salarioBruto - descIR
elif salarioBruto <= 2500:
    # desconto de 10%
    descontoIR = 0.1
    descIR = salarioBruto * descontoIR
    salarioDesc = salarioBruto - descIR
else:
    # desconto de 20%
    descontoIR = 0.20
    descIR = salarioBruto * descontoIR
    salarioDesc = salarioBruto - descIR

# Desconto INSS de 10%
descontoINSS = 0.10
descINSS = salarioBruto * descontoINSS
salarioDesc = salarioBruto - descINSS

# Desconto FGTS de 11%
descontoFGTS = 0.11
descFGTS = salarioBruto * descontoFGTS
salarioDesc = salarioBruto - descFGTS

# Total dos descontos
totalDescontos = descIR + descINSS

# Salário líquido
salarioLiquido = salarioBruto - totalDescontos

print("\n******** FOLHA DE PAGAMENTO ********")
print(f"Salário bruto............ R$ {salarioBruto:.2f}")
print(f"(-) IR................... R$ {descIR:.2f}")
print(f"(-) INSS................. R$ {descINSS:.2f}")
print(f"(-) FGTS................. R$ {descFGTS:.2f}")
print(f"Total de descontos....... R$ {totalDescontos:.2f}")
print(f"Salário líquido.......... R$ {salarioLiquido:.2f}")
