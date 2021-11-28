from Compartilhados.Excecoes.valoresInvalidosException import ValoresInvalidosException
import os
import copy
from Views.Compartilhados.UtilitariosView import utilitariosView
from Controladores.UsuariosControlador import UsuariosControlador
from Controladores.ProdutoresControlador import ProdutoresControlador

from Repositorio.Entidades.Usuario import Usuario


class UsuariosView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.usuariosControlador = UsuariosControlador()

    def createUsuario(self):
        u = self.utilView
        os.system('cls')
        usuario = self.receberAtributos()
        
        try:
            usuarioCriada = self.usuariosControlador.createUsuario(usuario)
            os.system('cls')
            u.printSeparador(f'{"="*70}')
            u.printSucesso('Usuario criado com sucesso!')
            self.imprimir([usuarioCriada])
        except Exception as ex:
            os.system('cls')
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao criar o usuario! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}') 
        os.system('pause')

    def readUsuario(self):
        os.system('cls')
        id_usuario = self.utilView.receberValor(chave="digite o id da usuario que deseja vizualizar", tipo=int, obrigatorio=True)
        self.imprimirUsuarios(id_usuario=id_usuario, resumido=False)
        os.system('pause')

    def imprimirUsuarios(self, id_usuario=None, resumido=True):
        u = self.utilView
        os.system('cls')
        usuarios = []
        try:
            if id_usuario != None:
                usuario = self.usuariosControlador.readUsuario(id_usuario)
                if usuario != None:
                    usuarios.append(usuario)
            else:
                usuarios = self.usuariosControlador.readUsuarios()

            if len(usuarios) > 0:              
                if resumido:
                    self.imprimirResumido(usuarios)    
                else:
                    self.imprimir(usuarios)
            else:
                u.printSeparador(f'{"="*70}') 
                u.printErro('Nenhum usuario encontrado!')
                u.printSeparador(f'{"="*70}')
        except Exception as ex:
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao buscar o(s) usuario(s)! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}')

    def updateUsuario(self, usuarioLogado):
        usuarioEmEdicao = copy.deepcopy(usuarioLogado)
        u = self.utilView 
        houveEdicao = False 
        while True:
            os.system('cls')
            self.imprimir([usuarioEmEdicao])
            u.printInstrucao('Digite o número da informação que deseja alterar: ')
            u.printOpcao('1', 'Nome')
            u.printOpcao('2', 'E-Mail')
            u.printOpcao('3', 'Senha')
            print('')
            u.printOpcao('0', 'Finalizar alteração')
            op = self.utilView.receberValor(chave="valor", tipo=int, obrigatorio=True, validos=lambda x: x in range(8))
            if op == 0:     
                break                
            else:
                if op == 1: 
                    valor = self.utilView.receberValor(chave="informe o seu novo nome", tipo=str, obrigatorio=True)
                    usuarioEmEdicao.setNome(valor)
                    houveEdicao = True
                elif op == 2: 
                    valor = self.utilView.receberValor(chave="informe o seu novo e-mail", tipo=str, obrigatorio=True, validos=lambda x:  self.usuariosControlador.validarFormatoEmail(x))
                    usuarioEmEdicao.setEMail(valor)
                    houveEdicao = True
                elif op == 3: 
                    senhaAntiga = self.utilView.receberValor(chave="valor da sua senha antiga", tipo=str, obrigatorio=True,  validos=lambda x:  self.usuariosControlador.validarEmailSenha(usuarioLogado.getEMail(), x) != None)
                    valor = self.utilView.receberValor(chave="informe a sua nova senha", tipo=str, obrigatorio=True)
                    usuarioEmEdicao.setSenha(valor)
                    houveEdicao = True     
                       

        if houveEdicao:            
            os.system('cls')
            self.imprimir([usuarioEmEdicao])
            u.printInstrucao('Deseja salvar as alterações?')
            u.printOpcao('1', 'Sim')
            u.printOpcao('2', 'Não')
            op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 3))
            if op == 1:
                os.system('cls')
                u.printSeparador(f'{"="*70}') 
                try:
                    self.usuariosControlador.updateUsuario(usuarioEmEdicao)
                    u.printSucesso('A usuario foi atualizado com sucesso!')  
                    usuarioLogado = copy.deepcopy(usuarioEmEdicao)
                except Exception as ex:
                    u.printErro('Erro ao atualizar o usuario! Tente novamente.')  
                    u.printErro(F'ERRO: {ex}')
                u.printSeparador(f'{"="*70}') 
                os.system('pause')                
                
        return usuarioLogado

    def deleteUsuario(self, usuarioLogado):
        u = self.utilView
        os.system('cls')
        self.imprimir([usuarioLogado])
        u.printInstrucao(f'Tem cereza que quer excluir a sua conta?')
        u.printOpcao('1', 'Sim')
        u.printOpcao('2', 'Não')
        op = self.utilView.receberValor(chave="resposta", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 3))
        if op == 1:
            os.system('cls')
            u.printSeparador(f'{"="*70}')
            try:
                self.usuariosControlador.deleteUsuario(usuarioLogado.getIdUsuario())
                u.printSucesso('O usuario foi removido com sucesso!')  
            except Exception as ex:
                u.printErro('Erro ao remover o usuario! Tente novamente.')  
                u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}') 
            os.system('pause')

    def imprimirMenu(self, usuarioLogado):
        u = self.utilView
        while True:
            os.system('cls')
            u.printTitulo('Seu Perfil')
            self.imprimir([usuarioLogado])
            u.printInstrucao('Qual operação deseja realizar?')
            u.printOpcao('1', 'Editar os seus dados')
            u.printOpcao('2', 'Excluir conta')
            print('')
            u.printOpcao('0', 'Sair')
            u.printSeparador(f'\n{"="*70}')
            
            op = self.utilView.receberValor(chave="opção", tipo=int, obrigatorio=True, validos=lambda x: x in range(0, 3))
            if op == 1:
                usuarioLogado = self.updateUsuario(usuarioLogado)
            elif op == 2:
                self.deleteUsuario(usuarioLogado)
                usuarioLogado = None
                break
            elif op == 0:
                break
        return usuarioLogado


    def imprimir(self, usuarios):
        u = self.utilView        
        for usuario in usuarios:
            u.printSeparador(f'='*70)
            self.utilView.imprimirAtributTitulo('Id', usuario.getIdUsuario(), ' ')
            self.utilView.imprimirAtributTitulo('Nome', usuario.getNome(), '\n')
            u.printSeparador('='*70)            
            self.utilView.imprimirAtributo('E-Mail', usuario.getEMail(), '\n')
            u.printSeparador(f'{"="*70}\n\n')
    
    def imprimirResumido(self, usuarios):   
        u = self.utilView     
        for usuario in usuarios:
            u.printSeparador('='*70)
            self.utilView.imprimirAtributTitulo('Id', usuario.getIdUsuario(), ' ')
            self.utilView.imprimirAtributTitulo('Nome', usuario.getNome(), '\n')
        u.printSeparador('='*70)
    
    def receberAtributos(self):
        u = self.utilView
        usuario = Usuario()
        atributos = ['nome', 'email', 'senha']
        for atributo in atributos:
            os.system('cls')
            self.imprimir([usuario])
            u.printInstrucao('Por favor digite as suas informações:')        
            usuario = self.receberAtributo(atributo, usuario)
        return usuario


    def receberAtributo(self, atributoChave, usuario):
        u = self.utilView
        
        if atributoChave == 'nome':
            usuario.setNome(self.utilView.receberValor(chave="nome", tipo=str, obrigatorio=True))          
        elif atributoChave == 'email':
            usuario.setEMail(self.utilView.receberValor(chave="email", tipo=str, obrigatorio=True, validos=lambda x:  self.usuariosControlador.validarFormatoEmail(x)))
        elif atributoChave == 'senha':
            usuario.setSenha(self.utilView.receberValor(chave="senha", tipo=int, obrigatorio=False))
        return usuario
        
    def realizarLogin(self):        
        u = self.utilView
        os.system('cls')
        u.printInstrucao('Por favor digite as suas informações:')        

        email = self.utilView.receberValor(chave="E-Mail", tipo=str, obrigatorio=True)
        senha = self.utilView.receberValor(chave="Senha", tipo=str, obrigatorio=True)
        os.system('cls')
        
        try:           
            usuario = self.usuariosControlador.validarEmailSenha(email, senha)
            if usuario == None:
                u.printSeparador(f'{"="*70}') 
                u.printErro('Usuário ou senha inválidos! Tente novamente.') 
                u.printSeparador(f'{"="*70}') 
                os.system('pause')
            return usuario
        except Exception as ex:
            u.printSeparador(f'{"="*70}') 
            u.printErro('Erro ao realizar o login! Tente novamente.')  
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}')             
            os.system('pause')
            os.system('cls')
            return None