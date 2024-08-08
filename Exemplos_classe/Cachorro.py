class Cachorro:
    ###SEMPRE COMEÇA PELO METODO CONSTRUTOS
    def __init__(self,nome,idade,peso,cor = "Preto"):
        self.nome =nome
        self.idade = idade
        self.peso = peso
        self.cor = cor
        #   #METODOS ... TODOS OS METODOS DEVEM TER COMO PARAMETRO SELF##
    def latir(self):
        print(f"{self.nome} AU AU AU")  
    
    def comer(self):
        print(f"{self.nome} comeu")
    
    def dormir(self):
        print("ZZZZZZ ZZZ ZZZZ ZZZ ZZ")
    
dog1 = Cachorro("Bilu",2,5,"Caramelo")
print(dog1)
print(dog1.nome)
print(dog1.cor)

dog2 =Cachorro("Belinha",2,5)
print(dog2)
print(dog2.nome)
print(dog2.cor)