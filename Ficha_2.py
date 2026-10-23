# EX. 1 --------------------------------------------------------------------------------------------------

# Principais métodos de listas utilizados
# • append(item): adiciona um novo elemento no final da lista
# • extend(lista): adiciona várias tarefas de uma vez
# • insert(pos, item): insere uma tarefa numa posição específica
# • remove(item): remove uma tarefa pelo seu conteúdo
# • pop(): remove a última tarefa ou pop(posição)
# • clear(): remove todas as tarefas
# • count(item): conta quantas vezes uma tarefa aparece
# • index(item): mostra a posição da tarefa
# • sort(): ordena a lista alfabeticamente
# • reverse(): inverte a ordem da lista
# • copy(): cria uma cópia da lista

# Programa simples para gerir uma lista de tarefas

tarefas = ["Estudar", "Lavar a loiça", "Fazer compras"]

while True:
    print("\nGESTOR DE TAREFAS")
    print("1- Adicionar tarefa")
    print("2- Adicionar várias tarefas")
    print("3- Inserir tarefa numa posição")
    print("4- Remover tarefa por nome")
    print("5- Remover última tarefa ou por índice")
    print("6- Remover todas as tarefas")
    print("7- Contar ocorrências")
    print("8- Ver índice de uma tarefa")
    print("9- Ordenar tarefas")
    print("10- Inverter ordem")
    print("11- Copiar lista")
    print("0- Sair")
    print("Lista atual:", tarefas)

    opcao = input("Escolha uma opção: ")

    if opcao == "1":
        tarefa = input("Digite a tarefa: ")
        tarefas.append(tarefa)

    elif opcao == "2":
        texto = input("Digite várias tarefas separadas por vírgula: ")
        lista_novas = [t.strip() for t in texto.split(",") if t.strip()]
        tarefas.extend(lista_novas)

    elif opcao == "3":
        posicao = int(input("Digite a posição: "))
        tarefa = input("Digite a tarefa: ")
        tarefas.insert(posicao, tarefa)

    elif opcao == "4":
        tarefa = input("Digite a tarefa a remover: ")
        tarefas.remove(tarefa)

    elif opcao == "5":
        escolha = input("Deseja remover a última tarefa (L) ou por índice (I)? ").upper()
        if escolha == "L":
            tarefas.pop()
        elif escolha == "I":
            indice = int(input("Digite o índice: "))
            tarefas.pop(indice)

    elif opcao == "6":
        tarefas.clear()

    elif opcao == "7":
        tarefa = input("Digite a tarefa: ")
        print("A tarefa aparece", tarefas.count(tarefa), "vezes.")

    elif opcao == "8":
        tarefa = input("Digite a tarefa: ")
        print("A tarefa está no índice:", tarefas.index(tarefa))

    elif opcao == "9":
        tarefas.sort()

    elif opcao == "10":
        tarefas.reverse()

    elif opcao == "11":
        copia = tarefas.copy()
        print("Cópia da lista:", copia)

    elif opcao == "0":
        print("Lista final:", tarefas)
        print("Até breve!")
        break

    else:
        print("Opção inválida.")


