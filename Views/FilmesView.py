from Views.ProdutoresView import ProdutoresView
from Compartilhados.Excecoes.valoresInvalidosException import ValoresInvalidosException
import os
from Views.Compartilhados.UtilitariosView import utilitariosView
from Controladores.FilmesControlador import FilmesControlador
from Controladores.ProdutoresControlador import ProdutoresControlador

from Repositorio.Entidades.Filme import Filme


class FilmesView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.filmesControlador = FilmesControlador()
        self.produtoresControlador = ProdutoresControlador()
        self.produtoresView = ProdutoresView()

    def createFilme(self):
        u = self.utilView
        os.system('cls')
        produtores = self.produtoresControlador.readProdutores()
        if len(produtores) > 0:
            filme = self.receberAtributos()
            
            try:
                filmeCriado = self.filmesControlador.createFilme(filme)
                os.system('cls')
                u.printSeparador(f'{"="*70}')
                u.printSucesso('Filme criado com sucesso!')
                self.imprimir([filmeCriado])
            except Exception as ex:
                os.system('cls')
                u.printSeparador(f'{"="*70}')
                u.printErro('Erro ao criar o filme! Tente novamente.')
                u.printErro(F'ERRO: {ex}')
                u.printSeparador(f'{"="*70}') 
        else:
            os.system('cls')
            u.printSeparador(f'{"="*70}')
            u.printErro('Não existe nenhum produtor cadastrado.\nCadastre um produtor antes de cadastrar um filme!')
            u.printSeparador(f'{"="*70}') 
        os.system('pause')

    def readFilme(self):
        os.system('cls')
        id_filme = self.utilView.receberValor(valorPrint="id do filme", chave="Digite o id do filme que deseja visualizar", tipo=int, obrigatorio=True)
        self.imprimirFilmes(id_filme=id_filme, resumido=False)
        os.system('pause')

    def imprimirFilmes(self, id_filme=None, resumido=True):
        u = self.utilView
        os.system('cls')
        filmes = []
        try:
            if id_filme != None:
                filme = self.filmesControlador.readFilme(id_filme)
                if filme != None:
                    filmes.append(filme)
            else:
                filmes = self.filmesControlador.readFilmes()

            if len(filmes) > 0:              
                if resumido:
                    self.imprimirResumido(filmes)    
                else:
                    self.imprimir(filmes)
            else:
                u.printSeparador(f'{"="*70}') 
                u.printErro('Nenhum filme encontrado!')
                u.printSeparador(f'{"="*70}')
        except Exception as ex:
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao buscar o(s) filme(s)! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}')

    def updateFilme(self):
        u = self.utilView
        os.system('cls')
        self.imprimirFilmes()        
        idFilme = self.utilView.receberValor(valorPrint="id do filme", chave="Informe o id do filme que será alterado (Digite 0 para cancelar)", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or self.filmesControlador.readFilme(x) != None )        
        if idFilme != 0:
            filme = self.filmesControlador.readFilme(idFilme)
            
            while True:
                os.system('cls')
                self.imprimir([filme])
                u.printInstrucao('Digite o número da informação que deseja alterar: ')
                u.printOpcao('1', 'Titulo')
                u.printOpcao('2', 'Produtor')
                u.printOpcao('3', 'Diretor')
                u.printOpcao('4', 'Ano de Lançamento')
                print('')
                u.printOpcao('0', 'Finalizar alteração')
                op = self.utilView.receberValor(chave="valor", tipo=int, obrigatorio=True, validos=lambda x: x in range(8))
                if op == 0:     
                    break                
                else:
                    if op == 1: 
                        valor = self.utilView.receberValor(chave="Informe o novo titulo do filme", tipo=str, obrigatorio=True)
                        filme.setTitulo(valor)
                    elif op == 2: 
                        self.produtoresView.imprimirProdutores(resumido=True)
                        valor = self.utilView.receberValor(chave="Informe o id do novo produtor", tipo=int,)
                        filme.setIdProdutor(valor)
                    elif op == 3: 
                        valor = self.utilView.receberValor(chave="Informe o nome do novo diretor", tipo=str,)
                        filme.setDiretor(valor)
                    elif op == 4:  
                        valor = self.utilView.receberValor(chave="Informe o novo ano de lançamento do filme", tipo=str,)
                        filme.setAnoLancamento(valor)
                    


            os.system('cls')
            self.imprimir([filme])
            u.printInstrucao('Deseja salvar as alterações?')
            u.printOpcao('1', 'Sim')
            u.printOpcao('2', 'Não')
            op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 3))
            if op == 1:
                os.system('cls')
                u.printSeparador(f'{"="*70}') 
                try:
                    self.filmesControlador.updateFilme(filme)
                    u.printSucesso('O filme foi atualizado com sucesso!')  
                except Exception as ex:
                    u.printErro('Erro ao atualizar o filme! Tente novamente.')  
                    u.printErro(F'ERRO: {ex}')
                u.printSeparador(f'{"="*70}') 
                os.system('pause')

    def deleteFilme(self):
        u = self.utilView
        os.system('cls')
        self.imprimirFilmes()
        idFilme = self.utilView.receberValor(valorPrint ="id do filme", chave="informe o id do filme que será removido (Digite 0 para cancelar)", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or self.produtoresControlador.readFilme(x) != None )
        if idFilme != 0:
            self.imprimirFilmes(idFilme, False)
            u.printInstrucao(f'Tem certeza que deseja excluir este filme?')
            u.printOpcao('1', 'Sim')
            u.printOpcao('2', 'Não')
            op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 3))
            if op == 1:
                os.system('cls')
                u.printSeparador(f'{"="*70}')
                try:
                    self.produtoresControlador.deleteFilme(idFilme)
                    u.printSucesso('O filme foi removido com sucesso!')  
                except Exception as ex:
                    u.printErro('Erro ao remover o filme! Tente novamente.')  
                    u.printErro(F'ERRO: {ex}')
                u.printSeparador(f'{"="*70}') 
                os.system('pause')

    def imprimirMenu(self):
        u = self.utilView
        while True:
            os.system('cls')
            u.printTitulo('Gerenciamento de Filmes')
            u.printInstrucao('Qual operação deseja realizar?')
            u.printOpcao('1', 'Criar um filme novo')
            u.printOpcao('2', 'Buscar um filme')
            u.printOpcao('3', 'Listar todos os filmes')
            u.printOpcao('4', 'Atualizar um filme')
            u.printOpcao('5', 'Remover um filme')
            print('')
            u.printOpcao('0', 'Sair')
            u.printSeparador(f'\n{"="*70}')
            
            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 6))
            if op == 1: 
                self.createFilme()
            elif op == 2:
                self.readFilme()
            elif op == 3:
                self.imprimirFilmes(resumido=False)
                os.system('pause')
            elif op == 4:
                self.updateFilme()
            elif op == 5:
                self.deleteFilme()
            elif op == 0:
                break


    def imprimir(self, filmes, filmesDTO=False):
        u = self.utilView        
        for filme in filmes:
            u.printSeparador(f'='*70)
            self.utilView.imprimirAtributTitulo('Id', filme.getIdFilme(), ' ')
            self.utilView.imprimirAtributTitulo('Titulo', filme.getTitulo(), '\n')
            u.printSeparador('='*70)
            if filmesDTO:
                produtorNome = filme.getNomeProdutor()
            else:
                try:
                    produtorNome = self.produtoresControlador.readProdutor(filme.getIdProdutor()).getNome() 
                except ValoresInvalidosException as ex:
                    produtorNome = 'Desconhecido'
            self.utilView.imprimirAtributo('Produtor', produtorNome, '\n')
            self.utilView.imprimirAtributo('Diretor', filme.getDiretor(), '\n')
            self.utilView.imprimirAtributo('Titulo', filme.getTitulo(), '\n')
            self.utilView.imprimirAtributo('Data Lançamento', filme.getAnoLancamento(), '\n')
           
            u.printSeparador(f'{"="*70}\n\n')
    
    def imprimirResumido(self, filmes):   
        u = self.utilView     
        for filme in filmes:
            u.printSeparador('='*70)
            self.utilView.imprimirAtributTitulo('Id', filme.getIdFilme(), ' ')
            self.utilView.imprimirAtributTitulo('Titulo', filme.getTitulo(), '\n')
        u.printSeparador('='*70)
    
    def receberAtributos(self):
        u = self.utilView
        filme = Filme()
        atributos = ['titulo', 'produtor', 'diretor', 'ano_lancamento']
        for atributo in atributos:
            os.system('cls')
            self.imprimir([filme])
            u.printInstrucao('Por favor digite as informações do novo filme:')        
            filme = self.receberAtributo(atributo, filme)
        return filme


    def receberAtributo(self, atributoChave, filme):
        u = self.utilView
        
        if atributoChave == 'titulo':
            filme.setTitulo(self.utilView.receberValor(chave="titulo", tipo=str, obrigatorio=True))  
        elif atributoChave == 'produtor':
            self.produtoresView.imprimirProdutores(resumido=True)        
            filme.setIdProdutor(self.utilView.receberValor(chave="produtor", tipo=int, obrigatorio=False, validos=lambda x: self.produtoresControlador.readProdutor(x) != None ))
        elif atributoChave == 'diretor':
            filme.setDiretor(self.utilView.receberValor(chave="diretor", tipo=str, obrigatorio=True))
        elif atributoChave == 'ano_lancamento':
            filme.setAnoLancamento(self.utilView.receberValor(chave="ano_lancamento", tipo=str, obrigatorio=True))
        return filme
        
        