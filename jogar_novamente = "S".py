jogar_novamente = "S"

while jogar_novamente.upper() == "S":
    numero_secreto = randint(1, 100)
    tentativas = 0
    acertou = False
    pontuacao = 0
    
    print("\nJogo Iniciado! Tente adivinhar o número entre 1 e 100.")
    
    while tentativas < 7 and not acertou:
        palpite = int(input("Introduza o seu palpite: "))
        
        # Impede valores inferiores a 1 ou superiores a 100
        if palpite < 1 or palpite > 100:
            print("Valor inválido! Insira um número entre 1 e 100.")
            continue
            
        # Contabilizar o número de tentativas
        tentativas += 1
        
        if palpite == numero_secreto:
            acertou = True
            # Informar quando o jogador acertar
            print("Parabéns! Você acertou no número!")
        elif numero_secreto > palpite:
            print("O número gerado aleatoriamente é maior.")
        else:
            print("O número gerado aleatoriamente é menor.")
            
    # Sistema de pontuação
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
        
    # Apresentar a pontuação final
    print(f"Pontuação final: {pontuacao} pontos")
    
    # No final deve perguntar: Deseja jogar novamente? (S/N)
    jogar_novamente = input("Deseja jogar novamente? (S/N): ")

print("Jogo terminado. Obrigado!")