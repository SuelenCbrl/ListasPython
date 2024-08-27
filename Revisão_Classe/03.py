class Pessoa:  ##  SUPER CLASSE ##
    def __init__(self,nome,endereco,telefone,idade=0):
        self.__name =nome  ## ATRIBUTO PRIVADO 
        self.local = endereco
        self.fone = telefone
        self.idade= idade

    def getNome(self):
        return self.__name
    
    def setNome(self,novo_nome):
        self.__name = novo_nome
    
    def verificaIdade(self):
        if self.idade >18:
            return True
        else:
            return False
    
    def getEndereco(self):
        return self.local
    
    def setEnderco(self,novo_local):
        self.local = novo_local

    def getFone(self):
        return self.fone
    
    def setFone(self,novo_fone):
        self.fone = novo_fone
   
p1=Pessoa("Joao","Av Afonso","9999",17)
print(p1.getNome())

p1.setNome("Thiago Almeida")
print(p1.getNome())

p1.setEnderco("Av Eng Amelio")
print(p1.getEndereco())

p1.setFone("889977")
print(p1.getFone())

teste = p1.verificaIdade()
print(teste)

### ooouuuu ##

# nomepessoa = p1.getNome()
# print(nomepessoa)


