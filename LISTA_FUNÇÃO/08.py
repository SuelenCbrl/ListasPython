def peixe():
    multa = excesso + 4
    excesso = quant -50
    if quant > 50:
        print("Excesso, Multa de R$",multa)
    else:
        print("Dentro do regulamento")


quant = float(input("Digite peso total pescado: "))

print(peixe)