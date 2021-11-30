from Views.SobreView import SobreView
from Repositorio.Entidades.Usuario import Usuario
from Views.UsuariosView import UsuariosView
import os
from Views.MenuPrincipalView import MenuPrincipalView
from Views.Compartilhados.UtilitariosView import utilitariosView


class MenuLoginView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.menuPrincipalView = MenuPrincipalView()
        self.usuariosView = UsuariosView()
        self.SobreView = SobreView()
        
    def iniciarMenuLogin(self):
        u = self.utilView
        while True:
            os.system('cls')
            u.printTitulo('(ﾉ◕ヮ◕)ﾉ*:･ﾟ✧ Tela Inicial - Gerenciamento de filmes')
            u.printInstrucao('Escolha uma das operações abaixo:')
            u.printOpcao('1', 'Logar no sistema')
            u.printOpcao('2', 'Criar uma conta')
            u.printOpcao('3', 'Sobre')
            print('')
            u.printOpcao('0', 'Sair')
            u.printSeparador(f'\n{"="*70}')

            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 4))
            if op == 1:
                usuarioLogado = self.usuariosView.realizarLogin()      
                if usuarioLogado != None:         
                    self.menuPrincipalView.iniciarMenuPrincipal(usuarioLogado)    
            elif op == 2:
                self.usuariosView.createUsuario()
            elif op == 3:
                self.SobreView.imprimirSobre()
            elif op == 0:
                os.system('cls')
                u.printInstrucao('Finalizando... volte sempre!')
                break
            