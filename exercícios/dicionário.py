aluno= {
    "nome": "Carlos",
    "idade": 17, 
    "cidade":"Famalicao",
    "disciplinas":["Matematica", "Programacao", "ingles"],
    "notas":{"Matematica":[17.5,12], "Programacao":[18.25,13], "ingles":[12.25,7.75]}
}#dicionário

# Média de todas as notas 
soma = 0
no_notas = 0 
for notas_disciplina in aluno["notas"].values():
    soma += sum(notas_disciplina)
    no_notas += len(notas_disciplina)
    media = sum(notas_disciplina)/len(notas_disciplina)
    print(f"A média de {notas_disciplina} é {media:.2f}")


#imprimir nome do aluno 
print(aluno["nome"])#Carlos

# Alterar o valor de uma chave
aluno["idade" ]= 18

# Inserir uma nova chave
aluno["estado_civil"] = "Solteiro"
print(aluno)

# Imprimir as características do aluno
for chave in aluno.keys():
    print(chave, end=" ")
print()

# Imprimir somente os valores
for valor in aluno.values():
    print(valor, end=" ")
print()

# Imprimir chave e valor
for chave, valor in aluno.items():
    print(f"{chave}: {valor}")

aluno["disciplinas"].append("Portugues")
for disciplina in aluno["disciplinas"]:
    print(disciplina)

# imprimir nota específica de uma disciplina
print (aluno["notas"]["Programacao"][1])#13


#Sum - somar todas as notas de uma disciplina
