def pot(x,y):
    res = x**y
    return res

print("Calcule a Potencia!")
base = int(input("Digite a base:"))
expoente = int(input("Digite o expoente:"))

x = pot(base,expoente)
print(x)