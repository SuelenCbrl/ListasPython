try: 
    num = int(input("Digite um numero: "))
    lidos = 0
    pares = 0
    while num != 0:
        lidos += 1
        if num % 2 != 1:
            print(f"{num} É par!!!")
            pares += 1
        else:
            print(f"{num} NÃo é par!!!")
        num = int(input("Digite um numero: "))
    print("Total de Numeros Lidos: ", lidos)
    print("Total De Pares", pares)
except:
    print("Entrada invalida!")