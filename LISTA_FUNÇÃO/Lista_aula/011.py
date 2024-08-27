# Crie uma função que receba como argumento uma lista, com
# valores de qualquer tipo. A função deve imprimir todos os
# elementos da lista numerando-os. 
frutas = ['pera','uva','maça','salada mista']

def imprima(lista):
    i = 0
    while i < len(lista):
        print(f'{i+1}.{lista[i]}')
        i +=1

def imprima2(lista):
    cont = 1
    for item in lista:
        print(f'{cont}.{item}')
        cont +=1


imprima(frutas)

