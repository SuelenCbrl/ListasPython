cont = 1
salario = 4000
atual= 0
while cont <= 4:
    atual =salario * 1.5
    print(f"Loop {cont} Valor: {atual}")
    salario += 2
    cont += 1
print(f"Total:", salario)