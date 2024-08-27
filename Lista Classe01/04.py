# Classe Conta: Um banco mantém contas de clientes armazenando o número da conta, o
# nome do cliente e o saldo atual da conta. Crie uma classe que modele um Conta-Corrente.
class Conta:
    def __init__(self, nome,cpf,numero,saldo):
        self.name =nome  
        self.cpf = cpf
        self.numero = numero
        self.saldo = saldo
   
    def hello(self):
        print(f"Olá {self.name}")

    
    def getSaldo(self):
        return self.saldo
    
    def setNome(self,novo_saldo):
        self.saldo = novo_saldo




conta1=Conta("Suelen",5642763164,25452,"R$900")
conta1.hello()
