i = 1
soma = 0
while i < 10:
    try:
        num = int(input("Digite um numero: "))
        soma += num
        print(soma)
        i+=1
    except:
        print("Entrada invalida!")
print("Soma: ",soma)
