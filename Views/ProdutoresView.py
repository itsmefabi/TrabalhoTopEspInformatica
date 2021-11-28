from Compartilhados.Excecoes.valoresInvalidosException import ValoresInvalidosException
import os
from Views.Compartilhados.UtilitariosView import utilitariosView
from Controladores.ProdutoresControlador import ProdutoresControlador

from Repositorio.Entidades.Produtor import Produtor


class ProdutoresView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.produtoresControlador = ProdutoresControlador()

    def createProdutor(self):
        u = self.utilView
        os.system('cls')
        produtor = self.receberAtributos()
        
        try:
            produtorCriado = self.produtoresControlador.createProdutor(produtor)
            os.system('cls')
            u.printSeparador(f'{"="*70}')
            u.printSucesso('Produtor criado com sucesso!')
            self.imprimir([produtorCriado])
        except Exception as ex:
            os.system('cls')
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao criar o produtor! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}') 
        os.system('pause')

    def readProdutor(self):
        os.system('cls')
        id_produtor = self.utilView.receberValor(valorPrint="id do produtor", chave="digite o id do produtor que deseja vizualizar", tipo=int, obrigatorio=True)
        self.imprimirProdutores(id_produtor=id_produtor, resumido=False)
        os.system('pause')

    def imprimirProdutores(self, id_produtor=None, resumido=True):
        u = self.utilView
        os.system('cls')
        produtores = []
        try:
            if id_produtor != None:
                produtor = self.produtoresControlador.readProdutor(id_produtor)
                if produtor != None:
                    produtores.append(produtor)
            else:
                produtores = self.produtoresControlador.readProdutores()

            if len(produtores) > 0:              
                if resumido:
                    self.imprimirResumido(produtores)    
                else:
                    self.imprimir(produtores)
            else:
                u.printSeparador(f'{"="*70}') 
                u.printErro('Nenhum produtor encontrado!')
                u.printSeparador(f'{"="*70}')
        except Exception as ex:
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao buscar o(s) produtor(s)! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}')

    def updateProdutor(self):
        u = self.utilView
        os.system('cls')
        self.imprimirProdutores()        
        idProdutor = self.utilView.receberValor(valorPrint="id do produtor", chave="informe o id do produtor que será alterado (Digite 0 para cancelar)", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or self.produtoresControlador.readProdutor(x) != None )        
        if idProdutor != 0:
            produtor = self.produtoresControlador.readProdutor(idProdutor)
            
            while True:
                os.system('cls')
                self.imprimir([produtor])
                u.printInstrucao('Digite o número da informação que deseja alterar: ')
                u.printOpcao('1', 'Nome')
                print('')
                u.printOpcao('0', 'Finalizar alteração')
                op = self.utilView.receberValor(chave="valor", tipo=int, obrigatorio=True, validos=lambda x: x in range(8))
                if op == 0:     
                    break                
                else:
                    if op == 1: 
                        valor = self.utilView.receberValor(chave="informe o novo valor de nome", tipo=str, obrigatorio=True)
                        produtor.setNome(valor)


            os.system('cls')
            self.imprimir([produtor])
            u.printInstrucao('Deseja salvar as alterações?')
            u.printOpcao('1', 'Sim')
            u.printOpcao('2', 'Não')
            op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 3))
            if op == 1:
                os.system('cls')
                u.printSeparador(f'{"="*70}') 
                try:
                    self.produtoresControlador.updateProdutor(produtor)
                    u.printSucesso('O produtor foi atualizado com sucesso!')  
                except Exception as ex:
                    u.printErro('Erro ao atualizar a produtor! Tente novamente.')  
                    u.printErro(F'ERRO: {ex}')
                u.printSeparador(f'{"="*70}') 
                os.system('pause')

    def deleteProdutor(self):
        u = self.utilView
        os.system('cls')
        self.imprimirProdutores()
        idProdutor = self.utilView.receberValor(valorPrint="id do produtor", chave="informe o id do produtor que será removido (Digite 0 para cancelar)", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or self.produtoresControlador.readProdutor(x) != None )
        if idProdutor != 0:
            self.imprimirProdutores(idProdutor, False)
            u.printInstrucao(f'Tem certeza que quer excluir esse produtor?')
            u.printOpcao('1', 'Sim')
            u.printOpcao('2', 'Não')
            op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 3))
            if op == 1:
                os.system('cls')
                u.printSeparador(f'{"="*70}')
                try:
                    self.produtoresControlador.deleteProdutor(idProdutor)
                    u.printSucesso('O produtor foi removido com sucesso!')  
                except Exception as ex:
                    u.printErro('Não é possivel remover um produtor vinculado a um filme.')  
                    u.printErro(F'ERRO: {ex}')
                u.printSeparador(f'{"="*70}') 
                os.system('pause')

    def imprimirMenu(self):
        u = self.utilView
        while True:
            os.system('cls')
            u.printTitulo('Manipulação de Produtores')
            u.printInstrucao('Qual operação deseja realizar?')
            u.printOpcao('1', 'Criar um produtor novo')
            u.printOpcao('2', 'Buscar um produtor')
            u.printOpcao('3', 'Listar todos os produtores')
            u.printOpcao('4', 'Atualizar um produtor')
            u.printOpcao('5', 'Remover um produtor')
            print('')
            u.printOpcao('0', 'Sair')
            u.printSeparador(f'\n{"="*70}')
            
            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 6))
            if op == 1: 
                self.createProdutor()
            elif op == 2:
                self.readProdutor()
            elif op == 3:
                self.imprimirProdutores(resumido=False)
                os.system('pause')
            elif op == 4:
                self.updateProdutor()
            elif op == 5:
                self.deleteProdutor()
            elif op == 0:
                break


    def imprimir(self, produtores):
        u = self.utilView        
        for produtor in produtores:
            u.printSeparador(f'='*70)
            self.utilView.imprimirAtributTitulo('Id', produtor.getIdProdutor(), ' ')
            self.utilView.imprimirAtributTitulo('Nome', produtor.getNome(), '\n')
            u.printSeparador(f'{"="*70}\n\n')
    
    def imprimirResumido(self, produtores):   
        u = self.utilView     
        for produtor in produtores:
            u.printSeparador('='*70)
            self.utilView.imprimirAtributTitulo('Id', produtor.getIdProdutor(), ' ')
            self.utilView.imprimirAtributTitulo('Nome', produtor.getNome(), '\n')
        u.printSeparador('='*70)
    
    def receberAtributos(self):
        u = self.utilView
        produtor = Produtor()
        atributos = ['nome']
        for atributo in atributos:
            os.system('cls')
            self.imprimir([produtor])
            u.printInstrucao('Por favor digite as informações do novo produtor:')        
            produtor = self.receberAtributo(atributo, produtor)
        return produtor


    def receberAtributo(self, atributoChave, produtor):
        u = self.utilView
        
        if atributoChave == 'nome':
            produtor.setNome(self.utilView.receberValor(chave="nome", tipo=str, obrigatorio=True))
        return produtor
        
        