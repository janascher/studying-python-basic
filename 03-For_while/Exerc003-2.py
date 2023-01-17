# Exercício 003-2:
#
# Faça um temporizador de segundos (contagem regressiva) que passe a atualizar o tempo mais raramente. A contagem com o intervalo entre cada atualização fique dois segundos maior após cada uma delas.
#
# Por exemplo, se ele iniciar o temporizador com 50 segundos, então receberá atualizações dizendo que faltam 50, 48, 44, 38, 30, 20 e 8 segundos (note que os intervalos entre as notificações foram 2, 4, 6, 8, 10 e 12 segundos).
#
# Desenvolva um programa que exiba em quais segundos o temporizador receberá atualizações, dado que o programa tenha sido inicializado com um tempo igual a N.
#
# Entrada:
# O seu programa deve receber um número inteiro positivo N, que é o tempo inicial do temporizador.
#
# Saída:
# Seu programa deve escrever a saída conforme os exemplos abaixo.
#
# Exemplos:
#
#       Entrada         Saída
#       10              Faltam 10 segundos
#                       Faltam 8 segundos
#                       Faltam 4 segundos
#                       Acabou
#       -----------------------------
#       50              Faltam 50 segundos
#                       Faltam 48 segundos
#                       Faltam 44 segundos
#                       Faltam 38 segundos
#                       Faltam 30 segundos
#                       Faltam 20 segundos
#                       Faltam 8 segundos
#                       Acabou

import time

interval = 2
n = int(input("\nTempo inicial do temporizador: "))

for i in range(n, -1, -interval):
    print(f"Faltam {i} segundos")
    time.sleep(interval)
    interval += 2
print("Acabou")
