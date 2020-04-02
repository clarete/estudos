# Iteravel é um tipo de variável que pode conter zero ou mais valores
#
# Sintaxe do for:
#
# for <variavel> in <iteravel>:
#    <body>

# exemplo1:
# pessoas = ["lincoln", "wanderson", "jusé", "Januário"]
# for pessoa in pessoas:
#     print(f"Oi {pessoa}")

# exemplo2:
numeros = [1, 2, 3, 4, 5]
pares = []   # lista vazia
impares = [] # lista vazia

# A funcão append do tipo de variável Lista adiciona um novo elemento
# à lista
numeros.append(6)
numeros.append(7)
numeros.append(8)

# O for itera sobre listas e iteraveis em geral. Em outras palavras,
# iterar significa percorrer um iterável item por item
for item in numeros:
    # O operador % retorna o resto da divisão. Se o resto da divisão
    # de um número por 2 for igual a zero, então podemos assumir que
    # este número é par!
    if item % 2 == 0:
        pares.append(item)
    else:
        impares.append(item)

print("Pares", pares)
print("Impares", impares)
