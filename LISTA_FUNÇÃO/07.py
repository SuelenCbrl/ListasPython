def salario(hora,base):
    res = hora *base

    if hora > 40:
        aument = res * 0.50
        print("Valor do Salario: ", aument)
    else:
        print("Valor do salario: ",res)
    return res

sal = int(input("Digite valor do salario base: "))
carga = int(input("Digite qunatidade de horas trabalhas: "))

x = salario(carga,sal)
print(x)