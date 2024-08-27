# Crie uma função que receba uma lista como argumento, os valores da lista 
#devem ser  numéricos, por fim retorne a média desses  valores.

numeros = [21,11,13,14,15,16,18,23,33]

def media(lista):
    return sum(lista)/len(lista)

resultado = media (numeros)
print(resultado)