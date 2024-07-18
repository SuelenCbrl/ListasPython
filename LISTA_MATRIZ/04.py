num = [10,20,30,10,20,30,10,20,30]
matriz= []

cont_linha = 0
coluna = 0
pos = 0
cont_coluna = 3

while cont_linha < 3: #cont_linha vai contar as linhas
    linha =[]
    while coluna < cont_coluna:#como deve pular 3 posições cont valo 3 enquanto coluna vale 0
        valor = num[pos] #Pos conta a posição que vamos pegar na lista 'num'
        linha.append(valor) #Adiciona a posição na lista 'lista'
        coluna += 1
        pos +=1
    matriz.append(linha) #Adiciona a linha criada na matriz
    cont_linha += 1
    cont_coluna += 3
print(num)
print(matriz)