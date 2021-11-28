from Servicos.ProdutoresServico import ProdutoresServico
from Compartilhados.utilitarios import utilitarios
from Compartilhados.Excecoes.valoresInvalidosException import ValoresInvalidosException
from Servicos.FilmesServico import FilmesServico


class FilmesControlador:
    def __init__(self):
        self.filmesServico = FilmesServico()
        self.produtorServico = ProdutoresServico()


    def createFilme(self, filme):
        self.validarConsistensiaDeFilme(filme)
        return self.filmesServico.createFilme(filme)

    def readFilmes(self):
        return self.filmesServico.readFilmes()
        
    def readFilme(self, id_filme):

        idValido = self.filmesServico.idValido(id_filme)
        if (not idValido):
            raise ValoresInvalidosException(mensagem=f"O id do filme informado não é válido!")

        return self.filmesServico.readFilme(id_filme)

    def updateFilme(self, filme):

        self.possuiId(filme.getIdFilme())

        self.validarConsistensiaDeFilme(filme)

        self.filmesServico.updateFilme(filme)

    def deleteFilme(self, id_filme):
        self.possuiId(id_filme)
        self.filmesServico.deleteFilme(id_filme)

    def validarConsistensiaDeFilme(self, filme):
        vlrsObrgNaoPreech = self.filmesServico.valoresObrigatoriosNaoPreenchidos(filme)
        if (len(vlrsObrgNaoPreech) > 0):
            raise ValoresInvalidosException(mensagem=f"Os valores a seguir são obrigatórios: {utilitarios.listarPorExtenso(vlrsObrgNaoPreech)}. Por favor, preencha-os.")

        tituloJaExiste = self.filmesServico.tituloJaExiste(filme)
        if (tituloJaExiste):
            raise ValoresInvalidosException(mensagem=f"O titulo informado já existe!")

        produtorNaoExiste = self.produtorServico.readProdutor(filme.getIdProdutor()) == None
        if (produtorNaoExiste):
            raise ValoresInvalidosException(mensagem=f"O filme informado não existe!")
    
    def possuiId(self, id_filme):
        possuiId = self.filmesServico.possuiId(id_filme)
        if (not possuiId):
            raise ValoresInvalidosException(mensagem=f"O id do filme informado não é válido!")