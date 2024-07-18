matriz = []

l = 3
c = 3

a=1
i=0
while i< l:
    linha = []
    j = 0
    while j< c:
        linha.append(a)
        a += 1
        j += 1
    matriz.append(linha)
    i += 1

x =0
while x < len(matriz):
    print(matriz[x])
    x +=1