class Usuario:
    id_usuario = None
    email = None
    nome = None
    senha = None

    def getIdUsuario(self):
        return self.id_usuario
    def setIdUsuario(self, id_usuario):
        self.id_usuario = id_usuario

    def getEMail(self):
        return self.email
    def setEMail(self, email):
        self.email = email
    
    def getNome(self):
        return self.nome
    def setNome(self, nome):
        self.nome = nome    
    
    def getSenha(self):
        return self.senha
    def setSenha(self, senha):
        self.senha = senha
    