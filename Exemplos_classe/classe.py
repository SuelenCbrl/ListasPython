#####classe pessoa
## abstração do objeto na programação 

###ATRIBUTOS NOME,IDADE,EMAIL,CIDADE
### METODOS comer, dormir,estudar(AÇOES-> FUNÇOES -> METODOS)

class Pessoa:
    def __init__(self,nome,idade,email,cidade):
        self.nome = nome
        self.idade = idade
        self.email = email
        self.cidade = cidade

    def oi(self):
        print(f'Olá {self.nome}')


###instanciar uma classe
        
pes1 = Pessoa("Joao",18,"joao@gmail.com","CG")
print(pes1.nome)
print(pes1.idade)

pes2 = Pessoa("Maria",52,"maria@gmail","RJ")
print(pes2.nome)
print(pes2.idade)