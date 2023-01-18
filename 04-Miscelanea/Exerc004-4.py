# Exercício 004-4:
#
# Implemente um programa denominado intercalador, que recebe duas strings e deve intercalá-las, alternando as letras de cada string, começando com a primeira letra da primeira string, seguido pela primeira letra da segunda string, em seguida pela segunda letra da primeira string, e assim sucessivamente. As letras restantes da cadeia mais longa devem ser adicionadas ao fim da string resultante e retornada.
#
# Observação: Seu programa não pode usar funções pré-definidas além de print(), input(), input().split(" ") e len().
#
# Dica: Utilize a função input().split(" ") para ler múltiplos elementos de uma string separadas por espaço e salvar em um vetor. No caso específico desse exercício, a ideia é obter um vetor de 2 strings da seguinte forma:
#
#       palavras = input().split(" ") (lendo um vetor de múltiplas strings (palavras) separadas por espaço)
#       S1 = palavras[0] # obtendo a primeira string
#       S2 = palavras[1] # obtendo a segunda string
#
# Entrada:
# Uma linha contendo duas cadeias de caracteres separadas por um espaço em branco.
#
# Saída:
# Uma cadeia de caracteres resultante da intercalação das duas cadeias fornecidas como entrada.
#
# Exemplos:
#
#       Entrada                      Saída
#       P2 I020..................... PI2020
#       aa bb....................... abab
#       13579 24680................. 1234567890
#       13579 24680................. 1234567890
#       1234567890987654321 abc..... 1a2b3c4567890987654321

print("\n", end="")

# Lê as duas strings
s1 = str(input("Insira a primeira string: "))
s2 = str(input("Insira a segunda string: "))

# Cria uma variável para armazenar a string resultante
resultado = ""

# Descobre qual é a string mais curta
if len(s1) > len(s2):
    menor_string = s2
    maior_string = s1
else:
    menor_string = s1
    maior_string = s2

# Intercala as letras das duas strings
for i in range(len(menor_string)):
    resultado += s1[i]
    resultado += s2[i]

# Adiciona as letras restantes da string mais longa ao final da string resultante
resultado = resultado + maior_string[len(menor_string):]

# Imprime a string resultante
print(
    f"\nResultado:"
    f"\n{resultado}"
)