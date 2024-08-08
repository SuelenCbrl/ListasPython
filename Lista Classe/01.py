# Classe Pessoa: Crie uma classe que modele uma pessoa. Esta classe deve possuir os
# seguintes atributos: Nome, idade, endereço; Deve conter os seguintes metodos: mostrar nome,
# alterar idade, imprimir endereço
class Pessoa:
    def __init__(self,nome,idade,endereco):
        self.nome = nome
        self.idade = idade
        self.cidade = endereco
    def mostrar_nome(self):
        return self.nome
    def editar_idade(self,novaidade):
        self.idade = novaidade
    def __str__(self):
        return f'nome={self.nome}, idade={self.idade}, cidade={self.cidade}'
x = Pessoa('Suelen',26,'Cg')
print(x)

x2 =(input("Gostaria de mudar a idade: 1 = sim // 2 = não"))
if x2 == "1":
    nova_idade = input("Digite o nova idade: ")
    x.editar_idade(nova_idade)
    print("Idade alterada com sucesso!")
    print(x)
else:
    print("Sem Alterações!")
    print(x)