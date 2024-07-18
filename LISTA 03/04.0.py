num_ava = int(input("Digite quantidade da avaliação: "))
lista = []
cont = 0
while cont < num_ava:
   nota =  int(input("Digite nota da avaliação:"))
   lista.append(nota)
   cont = cont +1
print(lista)
media = sum (lista) / len(lista)  
print(media)