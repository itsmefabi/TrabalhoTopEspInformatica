class Filme:
    id_filme = None
    id_produtor = None
    titulo = None
    diretor = None
    ano_lancamento = None

    def getIdFilme(self):
        return self.id_filme

    def setIdFilme(self, idfilme):
        self.id_filme = idfilme

    def getIdProdutor(self):
        return self.id_produtor
    def setIdProdutor(self, idProdutor):
        self.id_produtor = idProdutor
    
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
    
