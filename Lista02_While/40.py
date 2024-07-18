inicial = int(input("Digite o intervalo inicial: "))
final = int(input("Digite o intervalo final: "))
soma=0
if final < inicial:
    print("Intervalo de valores invalido!")
    #falta o else para o cod funcionar
else:
    while inicial <= final:
        if inicial % 2 == 1:
            soma += inicial
        inicial +=1
    print(soma)