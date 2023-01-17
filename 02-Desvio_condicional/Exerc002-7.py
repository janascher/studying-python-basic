# Exercício 002-7:

# O Hipermercado Tabajara está com uma promoção de carnes que é imperdível. Confira:
#                 Até 5 Kg                Acima de 5 Kg
# File Duplo      R$ 4,90 por Kg          R$ 5,80 por Kg
# Alcatra         R$ 5,90 por Kg          R$ 6,80 por Kg
# Picanha         R$ 6,90 por Kg          R$ 7,80 por Kg
# Para atender a todos os clientes, cada cliente poderá levar apenas 1 dos tipos de carne da promoção, porém não há limites para a quantidade de carne por cliente.
# Se compra for feita no cartão Tabajara o cliente receberá ainda um desconto de 5% sobre o total da compra.
# Escreva um programa que peça o tipo e a quantidade de carne comprada pelo usuário e gere um cupom fiscal, contendo as informações da compra: tipo e quantidade de carne, preço total, tipo de pagamento, valor do desconto e valor a pagar.

print("\n", end="")
print("*** PROMOÇÃO DE CARNES ***\n1- File Duplo\n2- Alcatra\n3- Picanha\n")
tipo = int(input("Digite o tipo de carne: "))
qtd = int(input("Digite a quantidade à comprar: "))
pgto = int(input("\nA forma de pagamento será no cartão Tabajara?\n1- Sim\n2- Não\nResposta: "))

#Tipo e quantidade de carne
if tipo == 1:
    nome = "File Duplo"
    if qtd <= 5:
        valor = qtd * 4.90
    else:
        valor = qtd * 5.80
elif tipo == 2:
    nome = "Alcatra"
    if qtd <= 5:
        valor = qtd * 5.90
    else:
        valor = qtd * 6.80
elif tipo == 3:
    nome = "Picanha"
    if qtd <= 5:
        valor = qtd * 6.90
    else:
        valor = qtd * 7.80
else:
    print("Tipo de carne inválido.")

#Forma de pagamento
if pgto == 1:
    resposta = "Sim"

    desconto = valor * 0.05
    total = valor - (desconto)
elif pgto == 2:
    resposta = "Não"
    desconto = 0
    total = valor
else:
    print("Forma de pagamento inválida.")


print("\n************* CUPOM FISCAL *************")
print(f"Carne............................. {nome}")
print(f"Quantidade........................ {qtd} Kg")
print(f"Valor total....................... R$ {valor:.2f}")
print(f"Pagamento no cartão Tabajara...... {resposta}")
print(f"Desconto.......................... R$ {desconto:.2f}")
print(f"Valor à pagar..................... R$ {total:.2f}")
