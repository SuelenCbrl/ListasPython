tra_lab = float(input("Digite Nota do Trabalho de Laboratorio: "))
av_sem = float(input("Digite Nota Da Avaliação Semestral: "))
ex_final = float(input("Digite Nota da Avaliação Final: "))

media = (tra_lab * 2) + (av_sem * 3) + (ex_final * 5)/10

if media <= 2.9:
  print("Média do Aluno: ",media)
  print("REPROVADO!!")

elif media >= 3 <= 5.9:
    print("Média do Aluno: ",media)
    print("RECUPERAÇÃO!")
    
else: 
    
    print("Média do Aluno: ",media)
    print("APROVADO!")