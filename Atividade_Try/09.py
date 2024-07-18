try:
    num = int(input("Digite um numero: "))
    i = num 
    lista = []
    while i >1:
        i =-1
        if num % i == 0:
            lista.append(i)
    print(sorted(lista))
    print(sum(lista))

except:
    print("Entrada Invalida!!")
   
