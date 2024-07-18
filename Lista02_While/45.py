salCarlos = 6000
salJoao = 2000
meses = 1
while salJoao <= salCarlos:
    salCarlos += salCarlos * 0.02
    salJoao += salJoao *0.05
    print(f"Mês: {meses} Salario do Carlos: {salCarlos}")
    print(f"Mês: {meses} Salario do João: {salJoao}")
    meses +=1
print("QTDE DE MESES: ",meses)
