def saudacao(nome,curso = "GPSI"):
     print(f"Bem-vindo ao curso de {curso}, {nome}!")

saudacao("Carlos")


# hoteis = ...
# def funcao():
#     global hoteis

def criar_lista(*alunos):
    lista = []
    for aluno in alunos:
         lista.append(aluno)
    return [lista]

x = criar_lista("Ana","João")
y = criar_lista("Rui","Maria", "Fernando", "Isa")
z = criar_lista("A1","A2", "A3", "A4")
nova_lista = criar_lista(*z)
print(x,y, nova_lista)


def config(**configuracoes): # configuracooes, o ** indica que é um dicionário, recebe chave e valor
    for chave, valor in configuracoes.items():
        print(f"{chave}: {valor}")

config(memória = "16GB", disco = "SSD 256GB", sistema = "Windows 11")

dicionario = {"memoria": "8GB", "disco": "SSD 256GB", "sistema": "Ubunto"}
config(**dicionario) 


def maiores_dois_valores(n1,n2,n3):
    maior = n1
    maior2 = 0
    if n2 > maior and n2 > n3:
        maior = n2
        if n1 > n3:
            maior2 = n1
        else:
            maior2 = n3

    return (maior, maior2)

# Classe é um molde para criar objetos, e objetos são instâncias de uma classe. 
# Uma classe define atributos (características) e métodos (comportamentos) que os objetos dessa classe terão. 
# Por exemplo, uma classe "Carro" pode ter atributos como "cor", "modelo" e "ano", e métodos como "acelerar" e "frear". 
# Cada objeto criado a partir da classe "Carro" terá suas próprias características e poderá executar os métodos definidos na classe.