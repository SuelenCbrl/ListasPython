l = int(input("Digite a quantidade de linhas da matriz: "))
c = int(input("Digite a quantidade de colunas da matriz: "))
matriz = []

for i in range(l):
    linha = []
    for j in range(c):
        num =int(input("Digite um numero: "))
        linha.append(num)
    matriz.append(linha)

for item in matriz:
    print(item)