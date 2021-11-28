import re
from Repositorio.Repositorios.UsuariosRepositorio import UsuariosRepositorio


class UsuariosServico:

    def __init__(self):
        self.usuariosRepositorio = UsuariosRepositorio()

    def createUsuario(self, usuario):
        return self.usuariosRepositorio.createUsuario(usuario)
    
    def readUsuarios(self):
        return self.usuariosRepositorio.readUsuarios()
    
    def readUsuario(self, id_usuario):
        return self.usuariosRepositorio.readUsuario(id_usuario)

    def updateUsuario(self, usuario):
        self.usuariosRepositorio.updateUsuario(usuario)

    def deleteUsuario(self, id_usuario):
        self.usuariosRepositorio.deleteUsuario(id_usuario)

    def valoresObrigatoriosNaoPreenchidos(self, usuario):
        vlrsObrgNaoPreech = []

        if (usuario.getNome() == None or usuario.getNome() == ""):
            vlrsObrgNaoPreech.append(usuario.getNome())

        if (usuario.getSenha() == None or usuario.getSenha() == ""):
            vlrsObrgNaoPreech.append(usuario.getSenha())

        if (usuario.getEMail() == None or usuario.getEMail() == ""):
            vlrsObrgNaoPreech.append(usuario.getEMail())

        return vlrsObrgNaoPreech    
    
    def emailJaExiste(self, email):
        return self.usuariosRepositorio.emailJaExiste(email)

    def idValido(self, idUsuario):
        try:
            if idUsuario != None and int(idUsuario):
                return True
            else:
                return False    
        except:
            return False
    
    def possuiId(self, id_usuario):
        return id_usuario != None

    def validarEmailSenha(self, email, senha):
        return self.usuariosRepositorio.validarEmailSenha(email, senha)
    
    def validarFormatoEmail(self, email):
        regex = '^(\w|\.|\_|\-)+[@](\w|\_|\-|\.)+[.]\w{2,3}$'
        if(re.search(regex, email)):
            return True    
        else:
            return False
        