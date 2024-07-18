try: 
    n1 = float(input("Digite a Nota 01:"))
    n2 = float(input("Digite a Nota 02:"))
    n3 = float(input("Digite a Nota 02:"))

    media = (n1 *1 )+ (n2 * 1) +(n3 * 2 )/3 

    if media >=60:
        print("Média do Aluno: ",media)
        print("APROVADO!!")
    else:
        media <=60
        print("Média do Aluno: ",media)
        print("REPROVADO!")
except:
    print("Entrada inválida!")