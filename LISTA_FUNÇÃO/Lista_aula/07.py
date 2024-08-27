# Crie uma função que efetue o cálculo do salário e
# como retorno teremos o valor a ser pago conforme o
# número de horas trabalhadas. Considere a carga
# horária de 40h por semana como salário base, caso
# ultrapasse o limite de 40h, o funcionário deve receber
# 50% a mais por hora excedente.
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