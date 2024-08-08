# Classe Aluno: Crie uma classe que modele um aluno. Esta classe deve 
# possuir os seguintes atributos:Nome,RA,Nota1,Nota2, Nota3,Nota4. 
# A classe deve ter o seguinte metodo: Mostrar_situacao: (APROVADO/EXAME
# /REPROVADO). Considere que, nesse caso, a média final é calculada pela média
# aritmética simples de todas as notas e que o aluno é aprovado somente
# se obtiver média maior ou igual a sete. Exame entre 5 e 6.9. Reprovado 
# abaixo de 5  A situação será retornada a partir das notas obtidas pelo aluno.
class aluno:
    def __init__(self,nome,RA,*args):
        self.nome = nome
        self.RA = RA
        self.nota = args

    def situation(self):
        media = sum(self.nota)/len(self.nota)
        if media >=7:
            print("Arovado!")
            print(media)
        elif media <=5:
            print("Reprovado!")
            print(media)
        else:
            print("Exame!")
            print(media)
        
    # def __str__(self):
    #     return f'Nome do aluno:{self.nome}, RA:{self.RA}, Nota 1:{self.nota}'

t =input("Digite Nome do aluno: ")
x = int(input("Digite RA do aluno: "))
n1 =int(input("Digite Nota 1 do aluno: "))


aluno1 = aluno(t,x,n1)
print(aluno1)
print(aluno1.situation())