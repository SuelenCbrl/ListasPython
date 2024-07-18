i = 0
soma = 0
while i < 10:
    try:
        num = int(input("Digite um número: "))
        soma += num
        i += 1 
    except:
        print("Entrada inválida, digite novamente!")

print("SOMA: ",soma)
