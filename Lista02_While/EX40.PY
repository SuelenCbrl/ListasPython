inicio = int(input("Inicial: "))
final = int(input("Final: "))
soma = 0
if inicio >final:
    print("Intervalo de valores invalido")
else:
    while inicio <= final:
        if inicio % 2 ==1:
            soma += inicio
        inicio += 1
print(soma)