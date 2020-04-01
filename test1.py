idade = input("Digite sua idade(1): ")

# Se a variável idade não for composta somente por dígitos, pergunte
# novamente.
#if not idade.isdigit():
#    idade = input("Digite sua idade(2): ")

maximo_de_perguntas = 3
perguntado = 1

# Se a variável idade não for composta somente por dígitos, pergunte
# novamente até que o usuário responda com apenas números (o while
# repete!)
# while <logical-condition>:
#    <body>
#
# Quando `perguntado` for igual a 3 (que é o máximo de perguntas)
# a repeticão também é interrompida
while not idade.isdigit() and perguntado < maximo_de_perguntas:
    idade = input(f"Digite sua idade({perguntado+1}): ")
    perguntado = perguntado + 1

# variáveis booleanas
# True e False
# Operadores booleanos
# *  or: ou -- o que for verdadeiro
# * and: and = e -- os dois tem que ser verdadeiros
#
#  and  | True  | False
# ------|-------|------
# True  | True  | False
# False | False | False

# or    | True  | False
# ------|-------|------
# True  | True  | True
# False | True  | False

if perguntado == maximo_de_perguntas:
    print("Véi, cê num sabe a sua idade?!?!?")
    exit()

idade = int(idade)

import datetime
data_atual = datetime.datetime.now()
ano_atual = data_atual.year

print(f"Você nasceu em {ano_atual - idade}")
