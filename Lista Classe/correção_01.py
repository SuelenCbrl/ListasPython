class Pessoa:
    def __init__(self,nome,idade,endereco):
            self.nome=nome
            self.idade=idade
            self.endereco =endereco
    
    def mostrarnome(self):
          print(f'NOme{self.nome}')

    #metodo de alterar a idade
    def alterar_idade(self,novaidade):
          self.idade=novaidade

    def imprimirendereco(self):
          print(self.endereco)
          

pes1 = Pessoa("João",18,"Av Afonso P",666)
pes1.mostrarnome()

pes1.alterar_idade(36)

print(pes1.idade)

# alterar a idade sem precisar de uma funçao
pes1.idade=54
