listanotas = []
i = 1
nome = input("ATLETA: ")
nota = float(input("NOTA: "))

maior = nota 
menor = nota

while i <=6:
    if nota > maior:
        maior = nota 
    if nota < menor:
        menor =nota
    listanotas.append(nota)
    i +=1
    nota = float(input("Nota: "))

listanotas.remove(maior)
listanotas.remove(menor)

print("Atleta: ",nome)
print("MELHOR NOTA ",maior)
print("PIOR NOTA: ", menor)