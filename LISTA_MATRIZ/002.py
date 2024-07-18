matriz = []
linha = int(input("Linhas: "))
coluna = int(input("Colunas: "))

i = 0
while i < linha:
    lista = []
    j = 0
    while j < coluna:
        num = int(input(f"Lin- {i} Col-{j} \n Entrada de Dados: "))
        lista.append(num)
        j +=1
    matriz.append(lista)
    i +=1

x =0
while x < len(matriz):
    print(matriz[x])
    x +=1
