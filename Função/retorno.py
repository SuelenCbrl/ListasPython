def soma(x,y):
    res = x +y
    print(f"Resultado:{res}")

def somar(x,y):
    res = x+y
    return res

soma(10,12)
x = somar(22,22)
print(x)
print(somar(25,25))

if somar(50,51) > 100:
    print("Soma maior que 100")