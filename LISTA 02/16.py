h = 40.50
trabalho = float(input("Digite quantidade de horas trabalhadas:"))
sal = h * trabalho

if sal >= 2500:
    desc = sal * 0.11
    sal1 = sal - desc
    print("Seu sálario é: ", sal1)

else:
    sal <= 2500
    print("Seu salario é: ",sal)