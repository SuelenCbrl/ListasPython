numAva = int(input("Digite o numero de avaliacoes: "))

somaNotas = 0
for i in range(numAva):
    ##receber nota da primeira avaliação##
    nota = float(input("Digite nota da avaliação{}:".format(i+1)))
    somaNotas += nota

media = somaNotas / numAva
print(media)