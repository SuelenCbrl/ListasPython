cont = 0 #AUXILIAR -> OBJETIVO
soma = 0
while cont < 10:
    try: 
        num = int(input("Digite um numero:"))
        if num <0:
            print("caiu no IF")
            soma = soma + num 
            cont = cont + 1
        else:
            print("valor do cont: ",cont)
            print("valor da soma: ",soma)
            continue
    except:
        print("Entrada invalida!")
media = soma / cont
print("MEDIA: ",media)
