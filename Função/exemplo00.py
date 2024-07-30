def pot(x,y):
    res = x**x
    return res
def soma (n1,n2):
    res = n1 +n2
    return res
def mult(n1,n2):
    res = n1 * n2
    return res


print("Calcular Potencia!")
base = int(input("Digite a base:"))
exp = int(input("Digite o expoente:"))

x = pot(base,exp)
print(x)