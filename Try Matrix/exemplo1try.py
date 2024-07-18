########TRATAMENTO DE EXCEÇÃO

try:
    a = int(input("N1: "))
    b = int(input("N2: "))

    res = a + b
    print("RES: ",res)
except:
    print("Entrada inválida!!!!")
