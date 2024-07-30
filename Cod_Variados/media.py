n1 = float(input("Digite N1: "))
n2 = float(input("Digite N2: "))
n3 = float(input("Digite N3: "))
n4 = float(input("Digite N4: "))
media = (n1 + n2 + n3 + n4)/4

if media >= 7: 
    print(f"A média aritmética é {media}")
    print("Aprovado!!")

elif media < 7 and media >4:
    print("MEDIA = ", media)
    print("RECUPERAÇÃO!!!")

else:
    print("REPROVADO!!!")