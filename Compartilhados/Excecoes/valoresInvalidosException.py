class ValoresInvalidosException(Exception):
    def __init__(self, mensagem="Alguns valores informados são inválidos!"):
        self.message = mensagem
        super().__init__(self.message)