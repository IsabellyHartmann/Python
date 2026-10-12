from random import randint

num = []

num_par = 0
num_impar = 0

num_maior = 0
num_menor = 0

media = 0

for _ in range(30):
    y = randint(1,100)
    num.append(y)
    print(y)

print(f"A lista completa é:{num}")

for a in range(len(num)):
    if a % 2 == 0:
        num_par += 1
    else:
        num_impar += 1

    if a > media:
        media += 1

print(f"Números pares:{num_par}")
print(f"Números impar:{num_impar}")



print(f"O maior número:{num_maior}")
print(f"O menor número:{num_menor}")

#print(f"Média dos números:{media}")

