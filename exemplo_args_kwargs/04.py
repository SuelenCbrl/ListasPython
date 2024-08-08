                    #### PARAMETROS NOMEADOS####
def calcula(**kwargs):
    print(kwargs)
    val = kwargs['valor']
    porc = kwargs['porcentagem']
    resultado = val*porc/100

    return resultado

x = calcula(idade =18,cidade ='cg',valor = 1000, porcentagem = 25)
print(x)