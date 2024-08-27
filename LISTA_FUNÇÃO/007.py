# Crie uma função de um programa de teste para o cálculo do volume de uma 
# esfera. Sendo que o raio é passado por parâmetro
def vol(r):
    v = ((4 * 3) * (r**3)) /3
    print("Volume de uma esfera: ",v)

n =float(input("Digite um numero:"))

x = vol(n)
print(x)