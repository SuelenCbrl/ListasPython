# Crie uma função que receba a altura e o raio de um cilindro circular e 
# retorne o volume do cilindro. O volume de um cilindro circular e calculado 
# por meio da seguinte fórmula: V = π * raio2 * altura, onde π = 3.141592
def vol(alt,raio):
    v = (3.141592 * (raio**2)) * alt
    print("Volume do cilindro: ",v)

r =float(input("Digite raio do cilindro:"))
alt =float(input("Digite altura do cilindro:"))

x = vol(r,alt)
print(x)