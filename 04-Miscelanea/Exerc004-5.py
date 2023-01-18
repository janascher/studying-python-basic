# Exercício 004-5:
#
# Um pantograma ou pangrama (do grego, pan ou pantós = todos, + grama = letra) é uma frase em que são usadas todas as letras do alfabeto de determinada língua.
#
# Crie um programa que permita verificar se uma frase é ou não um pantograma. Considere que o usuário digitará apenas uma frase.
#
# Entrada:
# A entrada contém uma frase sem acentos que pode ter letras maiúsculas ou minúsculas, ou sinais de pontuação.
#
# Saída:
# O programa deve imprimir SIM se a frase corresponde a um pantograma. Caso contrário, o programa deve imprimir NAO (sem acento).
#
# Exemplos:
#
#  Entrada                                                  Saída
#  Quem traz CD, LP, fax, engov e whisky JB?............... SIM
#  Bancos futeis pagavam-lhe queijo, whisky e xadrez....... SIM
#  The quick brown fox jumps over the lazy dog............. SIM
#  El veloz murcielago hindu comia feliz cardillo y kiwi....SIM
#  Esta frase nao eh um pantograma......................... NAO

print("\n", end="")
frase = str(input("Insira uma frase: "))

# Remove os caracteres especiais e transforma todas as letras em minúscula (peguei da internet)
frase = "".join(c for c in frase if c.isalnum() or c.isspace()).lower()

alfabeto = "abcdefghijklmnopqrstuvwxyz"

for letra in alfabeto:
    if letra not in frase:
        print("NAO")
        break
else:
    print("SIM")