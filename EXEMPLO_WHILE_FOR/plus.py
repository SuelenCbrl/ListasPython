lista= []
cont = 0
while cont < 10:
    num = int(input("digite um numero: "))
    lista.append(num)
    cont = cont + 1

print(lista)
print(sum(lista))
print(sum(lista)/len(lista))