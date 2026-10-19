# EX. 1 --------------------------------------------------------------------------------------------------
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


# EX. 2 --------------------------------------------------------------------------------------------------

alunos = []

aluno_aprovado = 0
aluno_reprovado = 0
aluno_acima_media = 0

for _ in range(15):
    nota = randint(0,20)
    alunos.append(nota)
    if nota >= 10:
        aluno_aprovado +=1
    else:
        aluno_reprovado +=1
    if nota >= 16:
        aluno_acima_media +=1

soma= sum(alunos)
aluno_nota_maior=max(alunos)
aluno_nota_menor=min(alunos)
media= soma/len(alunos)


print(f"A maior nota: {aluno_nota_maior}")
print(f"A menor nota:{aluno_nota_menor}")
print(f"Média das notas:{round(media,2)}")
print (f"Alunos aprovados:{aluno_aprovado}")
print (f"Alunos reprovados:{aluno_reprovado}")
print (f"Alunos acima da média:{aluno_acima_media}")

# EX. 3 --------------------------------------------------------------------------------------------------