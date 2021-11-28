from Compartilhados.utilitarios import utilitarios
from Compartilhados.Excecoes.valoresInvalidosException import ValoresInvalidosException
from Servicos.ProdutoresServico import ProdutoresServico


class ProdutoresControlador:
    def __init__(self):
        self.produtoresServico = ProdutoresServico()

    def createProdutor(self, produtor):
        self.validarConsistensiaDeProdutor(produtor)
        return self.produtoresServico.createProdutor(produtor)

    def readProdutores(self):
        return self.produtoresServico.readProdutores()

    def readProdutor(self, id_produtor):

        idValido = self.produtoresServico.idValido(id_produtor)
        if (not idValido):
            raise ValoresInvalidosException(
                mensagem=f"O id do produtor informado não é válido!")

        return self.produtoresServico.readProdutor(id_produtor)

    def readProdutorPorNome(self, nome):

        return self.produtoresServico.readProdutorPorNome(nome)

    def updateProdutor(self, produtor):

        self.possuiId(produtor.getIdProdutor())

        self.validarConsistensiaDeProdutor(produtor)

        self.produtoresServico.updateProdutor(produtor)

    def deleteProdutor(self, id_produtor):
        self.possuiId(id_produtor)
        self.produtoresServico.deleteProdutor(id_produtor)

    def validarConsistensiaDeProdutor(self, produtor):
        vlrsObrgNaoPreech = self.produtoresServico.valoresObrigatoriosNaoPreenchidos(
            produtor)
        if (len(vlrsObrgNaoPreech) > 0):
            raise ValoresInvalidosException(
                mensagem=f"Os valores a seguir são obrigatórios: {utilitarios.listarPorExtenso(vlrsObrgNaoPreech)}. Por favor, preencha-os.")

        nomeJaExiste = self.produtoresServico.nomeJaExiste(produtor)
        if (nomeJaExiste):
            raise ValoresInvalidosException(
                mensagem=f"O nome informado já existe!")
                
    def possuiId(self, id_produtor):
        possuiId = self.produtoresServico.possuiId(id_produtor)
        if (not possuiId):
            raise ValoresInvalidosException(
                mensagem=f"O id do produtor informado não é válido!")
