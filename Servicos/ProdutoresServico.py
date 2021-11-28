from Repositorio.Repositorios.ProdutoresRepositorio import ProdutoresRepositorio


class ProdutoresServico:

    def __init__(self):
        self.produtoresRepositorio = ProdutoresRepositorio()

    def createProdutor(self, produtor):
        return self.produtoresRepositorio.createProdutor(produtor)
    
    def readProdutores(self):
        return self.produtoresRepositorio.readProdutores()
    
    def readProdutor(self, id_produtor):
        return self.produtoresRepositorio.readProdutor(id_produtor)

    def readProdutorPorNome(self, nome):
        return self.produtoresRepositorio.readProdutorPorNome(nome)

    def updateProdutor(self, produtor):
        self.produtoresRepositorio.updateProdutor(produtor)

    def deleteProdutor(self, id_produtor):
        self.produtoresRepositorio.deleteProdutor(id_produtor)

    def valoresObrigatoriosNaoPreenchidos(self, produtor):
        vlrsObrgNaoPreech = []

        if (produtor.getNome() == None or produtor.getNome() == ""):
            vlrsObrgNaoPreech.append(produtor.getNome())

        return vlrsObrgNaoPreech    
    
    def nomeJaExiste(self, produtor):
        return self.produtoresRepositorio.nomeJaExiste(produtor)

    def idValido(self, idProdutor):
        try:
            if idProdutor != None and int(idProdutor):
                return True
            else:
                return False    
        except:
            return False
    
    def possuiId(self, id_produtor):
        return id_produtor != None
