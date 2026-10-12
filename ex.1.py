from random import randint

nums = []

num_par = 0
num_impar = 0
num_acima_media = 0

for _ in range(30):
    y = randint(1,100)
    nums.append(y)
    print(y)

soma= sum(nums)
num_maior=max(nums)
num_menor=min(nums)
media=soma/len(nums)
lista_media=[]

print(f"A lista completa é:{nums}")

for num in nums:
    if num % 2 == 0:
        num_par += 1
    else:
        num_impar += 1

    if num > media:
        num_acima_media += 1
        lista_media.append(num)

print(f"Números pares:{num_par}")
print(f"Números impar:{num_impar}")

print(f"O maior número: {num_maior}")
print(f"O menor número:{num_menor}")
print(f"Média dos números:{round(media,2)}")

print(f"Números acima da média: {num_acima_media} que são {lista_media}")
# soma = sum(num)
# maior = max(num)
# menor = min(num)
# media = soma/len(num)
