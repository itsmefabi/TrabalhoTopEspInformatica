from Views.Compartilhados.Estilos import Estilos


class utilitariosView:

    def __init__(self):
        self.estilos = Estilos()

    def imprimirAtributo(self, chave, valor, final):
        e = self.estilos
        print(f'{e.atributoChave(f"{chave}:")} {e.atributoValor(valor if valor != None else "Desconhecido"):>5}', end=final)

    def imprimirAtributTitulo(self, chave, valor, final):
        e = self.estilos
        print(f'{e.atributoChave(f"{chave}:")} {e.atributoValorTitulo(valor if valor != None else "Desconhecido"):>5}', end=final)

    def receberValor(self, valorPrint=None, chave="", tipo=None, obrigatorio=False, validos=None, larguraInt=23, casasDec=2):
        valorPrint = str(valorPrint) if valorPrint != None else chave
        
        while True:
            try:
                valor = self.inputValor(f'{chave.capitalize()}: ').strip()
                if obrigatorio and valor == "":
                    self.printErro(f'O {valorPrint.lower()} deve ser informado.')  
                    continue            
                if tipo == float and len(valor) > larguraInt:
                    self.printErro(f'O {valorPrint.lower()} deve ter no máximo {larguraInt - casasDec} casas inteiras e {casasDec} casas decimais.')  
                    continue
                if tipo == float and valor[::-1].find('.') > casasDec:
                    self.printErro(f'O {valorPrint.lower()} deve ter no máximo {casasDec} casas decimais.')  
                    continue  
                valor = None if valor == "" else tipo(valor)
                if validos != None and not validos(valor):
                    raise Exception()                                    
                return valor                
            except:
                self.printErro(f'O {valorPrint.lower()} informado está inválido. Por favor digite novamente.')
                continue       
            
    def printInstrucao(self, texto):
        e = self.estilos
        print(e.instrucao(texto), end='\n\n')
    
    def printOpcao(self, opcao, texto):
        e = self.estilos
        print(f'{e.opcao(f"{opcao} -")} {e.opcaoTexto(texto)}')
    
    def inputValor(self, texto):
        e = self.estilos
        return input(f'\n{e.digite(texto)}')
    
    def printErro(self, texto):
        e = self.estilos
        print(e.erro(texto))

    def printSucesso(self, texto):
        e = self.estilos
        print(e.sucesso(texto))
    
    def printSeparador(self, texto):
        e = self.estilos
        print(e.separador(texto))
    
    def printTitulo(self, texto):
        e = self.estilos
        print(e.titulo(f'{"="*70}\n{texto:^70}\n{"="*70}\n'))