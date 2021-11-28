class Estilos:
    
    def atributoChave(self, texto):
        return f'\033[1;33m{texto}\033[m'
    
    def atributoValor(self, texto):
        return f'\033[1;30m{texto}\033[m'

    def atributoValorTitulo(self, texto):
        return f'\033[1;37m{texto}\033[m'

    def instrucao(self, texto):
        return f'\033[1;36m{texto}\033[m'
    
    def opcao(self, texto):
        return f'\033[1;36m{texto}\033[m'
    
    def opcaoTexto(self, texto):
        return f'\033[1;37m{texto}\033[m'
    
    def digite(self, texto):
        return f'\033[1;33m{texto}\033[m'
    
    def erro(self, texto):
        return f'\033[1;31m{texto}\033[m'
    
    def sucesso(self, texto):
        return f'\033[1;32m{texto}\033[m'
    
    def separador(self, texto):
        return f'\033[1;33m{texto}\033[m'
    
    def titulo(self, texto):
        return f'\033[1;33m{texto}\033[m'