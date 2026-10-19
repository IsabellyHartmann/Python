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

print("---------------------------------------------------------------------------")

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

percentagem_aprovacao = (aluno_aprovado / len(alunos)) * 100

print (f"Alunos aprovados:{aluno_aprovado}")
print (f"Alunos reprovados:{aluno_reprovado}")
print (f"Alunos acima da média:{aluno_acima_media}")
print(f"A maior nota: {aluno_nota_maior}")
print(f"A menor nota:{aluno_nota_menor}")
print(f"Média das notas:{round(media,2)}")

print (f"Percentagem de aprovação:{round(percentagem_aprovacao,2)}%")
print("---------------------------------------------------------------------------")


# EX. 3 --------------------------------------------------------------------------------------------------

jogar_novamente = "S"

while jogar_novamente.upper() == "S":
    numero_secreto = randint(1, 100)
    tentativas = 0
    acertou = False
    pontuacao = 0
    
    print("\nJogo Iniciado! Tente adivinhar o número entre 1 e 100.")
    
    while tentativas < 7 and not acertou:
        palpite = int(input("Introduza o seu palpite: "))
        if palpite < 1 or palpite > 100:
            print("Valor inválido! Insira um número entre 1 e 100.")
            continue
            
        tentativas += 1
        
        if palpite == numero_secreto:
            acertou = True
            print("Parabéns! Você acertou no número!")
        elif numero_secreto > palpite:
            print("O número gerado aleatoriamente é maior.")
        else:
            print("O número gerado aleatoriamente é menor.")
            
    if acertou:
        if tentativas == 1:
            pontuacao = 100
        elif tentativas == 2:
            pontuacao = 80
        elif tentativas == 3:
            pontuacao = 60
        elif tentativas == 4:
            pontuacao = 40
        elif tentativas == 5:
            pontuacao = 30
        elif tentativas == 6:
            pontuacao = 20
        elif tentativas == 7:
            pontuacao = 10
    else:
        print(f"Esgotou as 7 tentativas! O número era {numero_secreto}.")
        pontuacao = 0

    print(f"Pontuação final: {pontuacao} pontos")
    jogar_novamente = input("Deseja jogar novamente? (S/N): ")
    
print("Jogo terminado. Obrigado!")