matriz = [[1,2,3],
          [4,5,6],
          [7,8,9]
         ]

nova_m = []
i=0
herme = 0
cont_lin = 0

while cont_lin < len(matriz):
    linha = []
    cont_col = 0

    while cont_col < len(matriz[i]):
        guil = matriz[herme][cont_col] *5
        linha.append(guil)
        cont_col +=1

    nova_m.append(linha)
    herme +=1
    cont_lin +=1

x = 0
while x < len(matriz):
    print(matriz[x])
    x +=1

bb = 0
while bb < len(nova_m):
    print(nova_m[bb])
    bb += 1