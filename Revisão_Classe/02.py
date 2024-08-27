class Pessoa:  ##  SUPER CLASSE ##
    def __init__(self,nome,endereco,telefone):
        self.name =nome  ## ATRIBUTO PRIVADO 
        self.local = endereco
        self.fone = telefone

    def hello(self):
        print(f"Olá {self.name}")

    def imprimeEndereco(self):
        print(self.local)


class PessoaFisica(Pessoa):## SubClasse da pessoa, os atributos vem meio que automatico##
    def __init__(self, nome, endereco, telefone,cpf,rg):
        super().__init__(nome, endereco, telefone)
        self.cpd = cpf
        self.rg =rg

class PessoaJuridica(Pessoa): ## SubClasse da super classe pessoa##
    def __init__(self, nome, endereco, telefone,cnpj,ie):
        super().__init__(nome, endereco, telefone)
        self.cnpj =cnpj
        self.ie = ie

    def hello(self): ### Polimorfismo -- pode reescrever um metodo herdado
        print(f"Olá PJ {self.name}  CNPF {self.cnpj}")

    def getCNPJ(self):
        return self.cnpj


p1= Pessoa("suelen","Av Eng Amelio","67999887755",)
p1.hello()

pes1 =PessoaFisica("joao","AV AFONSO PENA","9988","789","1235")       
pes1.hello()
pes1.imprimeEndereco()

empresa = PessoaJuridica("Claro","São Paulo", "11122223333","123456789999","77778888999")
empresa.hello()

empresa.imprimeEndereco()

print(empresa.getCNPJ())
