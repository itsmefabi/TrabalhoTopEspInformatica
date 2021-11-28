import os
from Controladores.GeralControlador import GeralControlador
from Views.Compartilhados.UtilitariosView import utilitariosView


class ExportacaoView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.geralControlador = GeralControlador()
    
    def exportarTodosOsDados(self):
        u = self.utilView
        os.system('cls')
        try:
            self.geralControlador.exportarTodosOsDados()
            u.printSeparador(f'{"="*70}') 
            u.printSucesso('Os dados foram exportados com sucesso!')  
            u.printSeparador(f'{"="*70}') 
        except Exception as ex:                    
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao exportar os dados! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}') 
        os.system('pause')
