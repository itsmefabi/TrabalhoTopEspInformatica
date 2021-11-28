from Repositorio.Entidades.Usuario import Usuario
from Repositorio.Conexao.conexao import ConexaoPostgre

class UsuariosRepositorio:
    def __init__(self):
        self.conexao = ConexaoPostgre()

    def createUsuario(self, usuario):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""INSERT INTO tb_usuario (                       
                      email, 
                      nome, 
                      senha
                  ) VALUES (
                      '{usuario.getEMail()}', 
                      '{usuario.getNome()}', 
                      '{usuario.getSenha()}'
                  ) RETURNING id_usuario;"""

        cur.execute(sql)        
        
        id_usuario = cur.fetchone()[0]  
        usuario.setIdUsuario(id_usuario) 

        con.commit()        
        con.close()

        return usuario

    def readUsuarios(self):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_usuario, 
                         email, 
                         nome,
                         senha                     
	              FROM tb_usuario;"""

        cur.execute(sql)  
        listaUsuarioBanco = cur.fetchall()
        listaUsuarioEntidade = self.converterListaBancoParaListaEntidade(listaUsuarioBanco)
        con.close()
        return listaUsuarioEntidade
        
    def readUsuario(self, id_usuario):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_usuario, 
                         email, 
                         nome,
                         senha                    
	              FROM tb_usuario
                  WHERE tb_usuario.id_usuario = {id_usuario}"""
        
        cur.execute(sql)  
        usuarioBanco = cur.fetchall()      
        con.close()
        
        if len(usuarioBanco) > 0:
            usuarioEntidade = self.converterBancoParaEntidade(usuarioBanco[0])
            return usuarioEntidade
        else:
            return None

    def updateUsuario(self, usuario):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""UPDATE tb_usuario
	              SET id_usuario={usuario.getIdUsuario()},
                      email='{usuario.getEMail()}', 
                      nome='{usuario.getNome()}', 
                      senha={usuario.getSenha()}
	              WHERE tb_usuario.id_usuario = {usuario.getIdUsuario()};"""

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        con.close()
        return usuario

    def deleteUsuario(self, id_usuario):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""DELETE FROM tb_usuario
	              WHERE tb_usuario.id_usuario = {id_usuario};"""

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        con.close()
    
    def converterBancoParaEntidade(self, usuarioBanco):
        usuarioEntidade = Usuario()
        usuarioEntidade.setIdUsuario(usuarioBanco[0])
        usuarioEntidade.setEMail(usuarioBanco[1])
        usuarioEntidade.setNome(usuarioBanco[2])
        usuarioEntidade.setSenha(usuarioBanco[3])
        return usuarioEntidade

    def converterListaBancoParaListaEntidade(self, listaUsuarioBanco):
        listaUsuarioEntidade = []
        for usuarioBanco in listaUsuarioBanco:
            listaUsuarioEntidade.append(self.converterBancoParaEntidade(usuarioBanco))
        return listaUsuarioEntidade
    
    def emailJaExiste(self, email):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT count(1)
	              FROM tb_usuario
                  WHERE tb_usuario.email = '{email}';"""

        cur.execute(sql)  
        qtdUsuarios = cur.fetchall()      
        con.close()
        
        if qtdUsuarios[0][0] > 0:            
            return True
        else:
            return False
    
    def validarEmailSenha(self, email, senha):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_usuario, 
                         email, 
                         nome,
                         senha                       
	              FROM tb_usuario
                  WHERE  tb_usuario.email = '{email}'
                  AND tb_usuario.senha = '{senha}'"""
        
        cur.execute(sql)  
        usuarioBanco = cur.fetchall()      
        con.close()
        
        if len(usuarioBanco) > 0:
            usuarioEntidade = self.converterBancoParaEntidade(usuarioBanco[0])
            return usuarioEntidade
        else:
            return None