cont = 1
soma = 0
while cont < 4:
    try:
        num = int(input("Digite um numero: "))
        soma =+ num
        cont =+ 1
    except:
        print("Entrada invalida! Digite novamente! ")
print("Soma = ",soma)
print("Cont = ",cont)
media =soma /cont
print(media)