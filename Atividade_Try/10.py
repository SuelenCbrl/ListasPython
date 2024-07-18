try:
    num = int(input("Digite um numero: "))
    cont =num
    maior =0
    menor = 9999999999999999999
    while cont >=1:
        f = int(input("Digite um  numero: "))
        if f > maior:
            maior = f
        if f < menor:
            menor = f
        cont -=1
except NameError:
    print("Entrada invalida!!!")

print("MAIOR ",maior)
print("MENOR ",menor)