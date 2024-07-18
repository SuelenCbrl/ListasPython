########TRATAMENTO DE EXCEÇÃO
i = 1
soma = 0

while i <= 10:
    try:
        num = int(input("Digite um numero: "))
        soma += num
        i += 1
    except:
        print("Entrada invalida, digite novamente!!!")

print("SOMA: ",soma)


