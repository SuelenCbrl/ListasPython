# Elabore uma função que receba três notas de um aluno como parâmetros e uma 
# letra. Se a letra for A, a função deverá calcular a média aritmética das 
# notas do aluno; se for P, deverá calcular a média ponderada, com pesos 5, 
# 3 e 2.
def nota(n1,n2,n3,tipo):
    if tipo == 'A':
        media = n1 +n2 + n3 /3
        return("média aritmética: ",media)
    elif tipo =='P':
        mediap = ((n1 * 5) +(n2 *3) + (n2 * 2))/10
        print("média ponderada: ",mediap)
    else :
        print("Invalido")
tipo = input("Digite A para média aritmética e P para média ponderada: ")
nota1 = input("Digite a media do aluno: ")
nota2 = input("Digite a media do aluno: ")
nota3 = input("Digite a media do aluno: ")

nota(nota1,nota2,nota3,tipo)