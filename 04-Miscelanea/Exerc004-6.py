# Exercício 004-6:
#
# Faça um programa que lê uma string e conta o número de vogais, consoantes, espaços e pontuações (caracteres “.”,“,”,“!”,“?”,"-").
#
# Observação: é proibido o uso de funções auxiliares, como o  count(), por exemplo.
#
# Entrada:
# Uma string podendo conter apenas vogais, consoantes, espaços e pontuações (caracteres “.”,“,”,“!”,“?”,"-").
#
# Saída
# A saída do programa deve ser a porcentagem de cada tipo de caractere na string, com 2 casas após a vírgula.
#
# Exemplos:
#
#  Entrada                            Saída
#  Um exercicio facil!............... Vogais: 42.11%
#                     ............... Consoantes: 42.11%
#                     ............... Espaços: 10.53%
#                     ............... Pontuações: 42.11%

print("\n", end="")
texto = str(input("Insira um texto: "))

vogais = 0
consoantes = 0
espaços = 0
pontuações = 0

for caracteres in texto:
    if caracteres in 'aeiou':
        vogais = vogais + 1

    elif caracteres in 'bcdfghjklmnpqrstvwxyz':
        consoantes += 1

    elif caracteres in '.,!?-':
        pontuações += 1

    else:
        espaços += 1

print(
    f"\n====== PORCENTAGEM DE CADA TIPO DE CARACTERE ======"
    f"\nVogais............. {vogais/len(texto)*100:.2f}%"
    f"\nConsoantes......... {consoantes/len(texto)*100:.2f}%"
    f"\nEspaços............ {espaços/len(texto)*100:.2f}%"
    f"\nPontuações......... {pontuações/len(texto)*100:.2f}%"
)