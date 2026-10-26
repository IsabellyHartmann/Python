# EX. 1 DICIONÁRIO --------------------------------------------------------------------------------------------------
# CRIAÇÃO E MANIPULAÇÃO BÁSICA

aluno= {
    "nome": "Ana Silva",
    "idade": 17, 
    "cidade":"Famalicao",
    "disciplinas":["Matematica", "Física", "Informática"],
    "notas":{"Matematica":18, "Física":17, "Informática":19}
}

aluno["disciplinas"].append("Português")
aluno["notas"]["Português"]= 16
aluno["idade"]= 18
print(aluno)

for disciplina, nota in aluno["notas"].items():
    print(f"Na disciplina de {disciplina} a nota foi de {nota}")


media_idade_alunos = 0.0

for notas in aluno.values():
   nome_aluno = aluno["nome"]
   notas_aluno = []
   for nota in aluno["notas"].values():
       notas_aluno.append(nota)
   media = round(sum(notas_aluno)/len(notas_aluno),2)
   print (f"Aluna {nome_aluno} teve média de {media} valores")


# EX. 2 DICIONÁRIO --------------------------------------------------------------------------------------------------
# # CONTAGEM DE FREQUÊNCIA


texto = "Isabelly Hartmann"
contagem = {}

for letra in texto:
    letra = letra.lower()
    if letra.isspace() == False:
        if letra in contagem.keys():
           contagem[letra] += 1
        else:
           contagem[letra] = 1

print(contagem)





# EX. 3 DICIONÁRIOS ANINHADOS --------------------------------------------------------------------------------------------------

biblioteca = {
    "livro1": {
        "titulo": "Python Fluente",
        "autor": "Luciano Ramalho",
        "ano": 2015,
        "disponivel": True
    },
    "livro2": {
        "titulo": "Pense em Python ",
        "autor": "Allen B. Downey",
        "ano": 2012,
        "disponivel": False
    },
    "livro3": {
        "titulo": "Introdução à programação com Python",
        "autor": "Nilo Ney Coutinho Menezes",
        "ano": 2019,
        "disponivel": True
        }
}

for livro in biblioteca.values():
    print(livro["titulo"])


biblioteca["livro4"] = {
        "titulo": "Programação com Python",
        "autor": "Marcelo Amorim",
        "ano": 2019,
        "disponivel": True
        }




# EX. 4 COMPREENSÃO DE DICIONÁRIOS  --------------------------------------------------------------------------------------------------