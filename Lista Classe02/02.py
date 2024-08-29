class Pessoa:
    def __init__(self, matricula,nome,idade):
        self.matricula=matricula
        self.nome=nome
        self.idade=idade
    
class Aluno(Pessoa):
    def __init__(self, matricula, nome, idade,nota,media):
        super().__init__(matricula, nome, idade)
        self.nota=nota
        self.media = media
    def estudar(self,estudar):
         print(f" {estudar} 3...2.....1...... Comece a estudar")


class Professor(Pessoa):
    def __init__(self, matricula, nome, idade):
        super().__init__(matricula, nome, idade)
        