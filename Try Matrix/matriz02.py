l = int(input("Digite a quantidade de linhas"))
c = int(input("Digite a quantidade de colunas"))
matriz = []

i = 0
while i < l:##criar linhas
    lista_linha = []
    j = 0
    while j < c:##preencher as colunas
        num = int(input("Digite um numero: "))
        lista_linha.append(num)
        j += 1
    matriz.append(lista_linha)
    i = i + 1

x = 0
while x < len(matriz):
    print(matriz[x])
    x += 1