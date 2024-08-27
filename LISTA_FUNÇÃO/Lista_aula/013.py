# Crie uma função que retorne uma lista com valor padrão. Para esta função,
# consideraremos como argumentos de entrada a quantidade de elementos e o 
# valor padrão a ser atribuído a todos eles. Exemplo de retorno:
# [1,1,1,1,1,1,1,1]
# [“A”,”A”,”A”,”A”]

def crialista(quant,valor):
    lista = []
    for i in range(quant):
        lista.append(valor)
    return lista

# print(crialista(10,'b'))
q = int(input("Digite tamanho da lista:"))
v = (input("Digite o valor especifico: "))

res = crialista(q,v)
print(res)