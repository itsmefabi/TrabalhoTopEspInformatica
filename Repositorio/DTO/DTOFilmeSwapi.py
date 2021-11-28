class DTOFilmeSwapi:
    id_filme = None
    nomeProdutor = None
    titulo = None
    diretor = None
    ano_lancamento = None
    

    def getIdFilme(self):
        return self.id_filme

    def setIdFilme(self, idfilme):
        self.id_filme = idfilme

    def getNomeProdutor(self):
        return self.nomeProdutor
    def setNomeProdutor(self, nomeProdutor):
        self.nomeProdutor = nomeProdutor
    
    def getTitulo(self):
        return self.titulo
    def setTitulo(self, titulo):
        self.titulo = titulo

    def getDiretor(self):
        return self.diretor
    def setDiretor(self, diretor):
        self.diretor = diretor
    
    def getAnoLancamento(self):
        return self.ano_lancamento
    def setAnoLancamento(self, ano_lancamento):
        self.ano_lancamento = ano_lancamento


    
