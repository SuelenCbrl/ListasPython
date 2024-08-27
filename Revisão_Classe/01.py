class Aluno:
    def __init__(self,nome,idade,email,nota=0):     #METODO CONSTRUTOR
        self.__nome = nome ## PRIVAR ATRIBUTO DA CLASSE ##
        self.idade = idade
        self.email = email
        self.nota = nota
    
    def hello(self):        ##METODO DA CLASSE
        print(f"Hello {self.nome}")

    def getIdade(self):
        return self.idade

a1 =Aluno('joao',18,'@gmail',7)
a2 =Aluno("Eliandro",30,'eli@gmail',10)


#Acessar os atributos#

# print(a1.nome)
# print(a1.idade)
# print(a1.email)
# print(a1.nota)


print(a2.idade)
a2.idade = 17 #trocar atributo
print(a2.idade)
a1.hello()
a2.hello()
idade = a2.getIdade()
# print(f"Idade que retornou do metodo {idade}")


if idade >18:
    print("Eliandro é maior!")
else:
    print("Eliandro é de fato menor!")
