matriz = [[1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1],
          [1,1,1,1,1,1,1,1]
          ]
z = 0
while z < len(matriz):
    print(matriz[z])
    z +=1

linha = int(input("Digite o numero da linha: "))
coluna = int(input("Digite o numero da coluna: "))

matriz[linha][coluna] = "x"


x = 0
while x < len(matriz):
    print(matriz[x])
    x +=1