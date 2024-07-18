#Ja começa entrando direto no while
#while True == While1

while True:
    r1 = int(input("R1: "))
    r2 = int(input("R2: "))
    if r1 ==0 or r2 ==0:
        break
    R = (r1*r2)/(r1 +r2)
    print("Resistencia: ",R)
print("PROGRAMA FINALIZADO")

