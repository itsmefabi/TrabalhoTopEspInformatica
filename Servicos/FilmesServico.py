from Repositorio.Repositorios.FilmesRepositorio import FilmesRepositorio


class FilmesServico:

    def __init__(self):
        self.filmesRepositorio = FilmesRepositorio()

    def createFilme(self, filme):
        return self.filmesRepositorio.createFilme(filme)
    
    def readFilmes(self):
        return self.filmesRepositorio.readFilmes()
    
    def readFilme(self, id_filme):
        return self.filmesRepositorio.readFilme(id_filme)

    def updateFilme(self, filme):
        self.filmesRepositorio.updateFilme(filme)

    def deleteFilme(self, id_filme):
        self.filmesRepositorio.deleteFilme(id_filme)

    def valoresObrigatoriosNaoPreenchidos(self, filme):
        vlrsObrgNaoPreech = []

        if (filme.getTitulo() == None or filme.getTitulo() == ""):
            vlrsObrgNaoPreech.append(filme.getTitulo())


        return vlrsObrgNaoPreech    
    
    def tituloJaExiste(self, filme):
        return self.filmesRepositorio.tituloJaExiste(filme)

    def idValido(self, idFilme):
        try:
            if idFilme != None and int(idFilme):
                return True
            else:
                return False    
        except:
            return False
    
    def possuiId(self, id_filme):
        return id_filme != None