from Views.UsuariosView import UsuariosView
from Views.ImportacaoView import ImportacaoView
import os
from Views.ExportacaoView import ExportacaoView
from Views.FilmesView import FilmesView
from Views.ProdutoresView import ProdutoresView
from Views.Compartilhados.UtilitariosView import utilitariosView


class MenuPrincipalView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.filmesView = FilmesView()
        self.produtoresView = ProdutoresView()
        self.exportacaoView = ExportacaoView()
        self.importacaoView = ImportacaoView()
        self.usuariosView = UsuariosView()


    def iniciarMenuPrincipal(self, usuarioLogado):
        u = self.utilView
        while True:
            os.system('cls')
            u.printTitulo('Menu Principal')
            u.printInstrucao('Qual operação deseja realizar?')
            u.printOpcao('1', 'Visualizar perfil')
            u.printOpcao('2', 'Gerenciar filme')
            u.printOpcao('3', 'Gerenciar produtor')
            u.printOpcao('4', 'Exportar todos os dados')
            u.printOpcao('5', 'Importar filme')
            print('')
            u.printOpcao('0', 'Sair')
            u.printSeparador(f'\n{"="*70}')

            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 6))
            if op == 1: 
                usuarioLogado = self.usuariosView.imprimirMenu(usuarioLogado)
                if usuarioLogado == None:
                    break 
            elif op == 2:
                self.filmesView.imprimirMenu()
            elif op == 3:
                self.produtoresView.imprimirMenu()
            elif op == 4:
                self.exportacaoView.exportarTodosOsDados()
            elif op == 5:
                self.importacaoView.importarFilme()
            elif op == 0:
                os.system('cls')
                u.printInstrucao('Finalizando... volte sempre!')
                break      
            