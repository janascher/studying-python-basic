# Exercício 002-5:

# As Organizações Tabajara resolveram dar um aumento de salário aos seus colaboradores. Eles contrataram você para desenvolver o programa que calculará os reajustes.
# Faça um programa que recebe o salário de um colaborador e o reajuste segundo o seguinte critério, baseado no salário atual:
# salários até R$ 280,00 (incluindo) : aumento de 20%
# salários entre R$ 280,00 e R$ 700,00 : aumento de 15%
# salários entre R$ 700,00 e R$ 1500,00 : aumento de 10%
# salários de R$ 1500,00 em diante : aumento de 5%
# Após o aumento ser realizado, informe na tela:
# o salário antes do reajuste;
# o percentual de aumento aplicado;
# o valor do aumento;
# o novo salário, após o aumento.

print("\n", end="")
salario = float(input("Informe o salário do colaborador: R$ "))

if salario <= 280:
    # aumento de 20%
    porcentagem = 0.20
    aumento = salario * porcentagem
    salarioNovo = salario + aumento
elif salario <= 700:
    # aumento de 15%
    porcentagem = 0.15
    aumento = salario * porcentagem
    salarioNovo = salario + aumento
elif salario <= 1500:
    # aumento de 10%
    porcentagem = 0.1
    aumento = salario * porcentagem
    salarioNovo = salario + aumento
else:
    # aumento de 5%
    porcentagem = 0.05
    aumento = salario * porcentagem
    salarioNovo = salario + aumento

print("\n************* REAJUSTE SALARIAL *************")
print(f"Salário antes do reajuste............. R$ {salario}")
print(f"Percentual de aumento aplicado........ {int(porcentagem * 100)} %")
print(f"Valor do aumento...................... R$ {aumento:.2f}")
print(f"Novo salário.......................... R$ {salarioNovo:.2f}")
