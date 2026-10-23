# EX. 1 --------------------------------------------------------------------------------------------------

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for num in lista:
    if num % 2 == 0:
        pares.append(num)

print("Versão com for:", pares)

pares_comp = [num for num in lista if num % 2 == 0]
print("Versão com list comprehension:", pares_comp)

# EX. 2 --------------------------------------------------------------------------------------------------

lista = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
pares = []

for num in lista:
    if num % 2 == 0:
        if num < 5:
            pares.append(num + 1)
        else:
            pares.append(num)

print("Versão com for:", pares)

pares_comp = [num + 1 if num < 5 else num for num in lista if num % 2 == 0]
print("Versão com list comprehension:", pares_comp)
