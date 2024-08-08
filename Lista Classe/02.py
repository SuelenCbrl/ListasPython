# Classe Livro: Crie uma classe que modele um Livro. Esta classe deve 
# possuir os seguintes atributos: Nome,autor,Editora,Paginas. A classe
# deve ter os seguintes metodos: alterar_editora() e listar_quant_paginas()

class livros:
    def __init__(self,nome_Livro,autor,editora,paginas): #Sintaxe metodo construtor#
        self.nome_Livro = nome_Livro
        self.autor = autor
        self.editora = editora
        self.paginas =paginas
    def editar_editora(self,novaeditora):
        self.editora = novaeditora
    def mostrar_nome(self):
        return self.nome_Livro
    def __str__(self):
        return f'Nome do Livro:{self.nome_Livro}, Autor:{self.autor}, editora:{self.editora}, quantodade de paginas:{self.paginas}'

x= (input("Digite Nome do livro: "))
y= (input("Digite o autor: "))
z= (input("Digite a editora: "))
x1 = int(input("Digite a quantidade de paginas: "))

livro1 = livros(x,y,z,x1)
print(livro1)

x2 =(input("Gostaria de mudar a editora: 1 = sim // 2 = não"))
if x2 == "1":
    nova_editora = input("Digite o novo nome da editora: ")
    livro1.editar_editora(nova_editora)
    print("Editora alterada com sucesso!")
    print(livro1)
else:
    print("Sem Alterações!")
    print(livro1)