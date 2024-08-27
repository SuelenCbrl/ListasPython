class livro:
    def __init__(self,nome,autor,editora,paginas):
        self.nome = nome 
        self.autor =autor
        self.editora =editora
        self.pagina=paginas
    def listaquantpagina(self):
        print(self.pagina)
    
    def alterareditora(self):
        print(self.pagina)

    def alterarEditora(self,novaeditora):
        self.editora = novaeditora

livro1 = livro("hobbit","tolken","galera",800)
#acessar atributos privados ou protegido criar um metodo de acesso -> getter
#editar atributos  privados ou protegido criar um metodo de acesso -> setter
