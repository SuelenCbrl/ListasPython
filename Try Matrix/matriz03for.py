l = int(input("Digite a quantidade de linhas: "))
c = int(input("Digite a quantidade de colunas: "))
matrix = []

for i in range(l):
    linha = []
    for j in range(c):
        num = int(input("Digite um numero: "))
        linha.append(num)
    matrix.append(linha)

for item in matrix:
    print(item)