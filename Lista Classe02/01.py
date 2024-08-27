class Filme:
    def __init__(self,nome,duracao):
        self.nome=nome
        self.duracao=duracao
    
    def play(self):
        print(f"{self.nome} Começou.....")
    
class FilmeAcao(Filme):
    def __init__(self, nome, duracao,produtora):
        super().__init__(nome, duracao)
        self.produtora = produtora
    
    def explodir(self,explosivo):
        print(f"ativar {explosivo} 3...2.....1...... BOOOOOOOMMM")

class FilmeDrama(Filme):
    def __init__(self, nome, duracao,produtora,ator):
        super().__init__(nome, duracao)
        self.produtora = produtora
        self.ator= ator
    
    def choro(self,choro):
        print(f"ativar {choro} 3...2.....1...... *-*")

class FilmeSuspense(Filme):
    def __init__(self, nome, duracao,produtora,ator):
        super().__init__(nome, duracao)
        self.produtora = produtora
        self.ator= ator
    
    def medo(self,medo):
        print(f" {medo} 3...2.....1...... Comece a rezar")


filme1 = Filme("TITANIC",300)
filme1.play

filme2 = FilmeAcao("RAMBO", 185, "PARAMOUNT")
filme2.play
filme2.explodir("TNT")

filme3 = FilmeDrama("A espera de um milagre",189,"Fox","Nicolas Cage")
filme3.play()
filme3.choro("*-*")

filme4 = FilmeSuspense("O exorcista",122,"Paramount", "Jason Miller" )
filme4.play()
filme4.medo("-.-")