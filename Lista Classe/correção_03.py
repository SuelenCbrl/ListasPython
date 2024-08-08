class Aluno:
    def __init__(self,nome,RA,*notas):
        self.__nome = nome
        self.ra =RA
        self.nota =notas

    def getNome(self):
        return self.__nome

    def setNome(self,novo_nome):
        self.__nome= novo_nome
        return True
    def situation(self):
        media = sum(self.nota)/len(self.nota)
        if media >=7:
            return f"{self.__nome} Aprovado ",media
            
        elif media <=5:
            return f"{self.__nome} Reprovado ",media
            
        else:
            return f"{self.__nome} Exame! ",media
       
    

a1=Aluno("joao",878,8,8,8,8)
print(a1.situation())