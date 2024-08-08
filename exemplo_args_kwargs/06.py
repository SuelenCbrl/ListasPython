def concatena (**kwargs):
    print(f'Valores recebidos: {kwargs}')
    resultado = ""
    for valor in kwargs.values():
        resultado += f'{valor} '
    return resultado

print(concatena(a="Python", b="Academy", c="Rules!"))