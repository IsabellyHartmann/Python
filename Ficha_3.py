# EX. 1 NúMEROS PARES --------------------------------------------------------------------------------------------------

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)

print("Versão com for:", pares)

pares_comp = [num for num in lista if num % 2 == 0]
print("Versão com list comprehension:", pares_comp)

# EX. 2 QUADRADOS DOS NÚMEROS --------------------------------------------------------------------------------------------------

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
quadrados = [num * num for num in lista]
print(quadrados)


# EX. 3 TAMANHOS DAS PALAVRAS --------------------------------------------------------------------------------------------------


lista = ["Python", "Java", "C++", "JavaScript"]
tamanhos = [len(palavra) for palavra in lista]

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

