palavra = input("Digite uma palavra: ")

print("Posicao de cada letra")
for i, letra, in enumerate(palavra):
    print("Posição {}: {}".format(i,letra))

print("Programa finalizado")