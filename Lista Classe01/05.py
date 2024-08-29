class circulo:
    def __init__(self,raio):
        self.raio=raio
    
    def calcularRaio(self,raio):
        area=3,14 *(raio*raio)
        print(area)


c1=circulo(9)
c1.calcularRaio()