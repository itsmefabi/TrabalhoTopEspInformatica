from Repositorio.Conexao.conexao import ConexaoPostgre
from Repositorio.Entidades.Produtor import Produtor


class ProdutoresRepositorio:
    def __init__(self):
        self.conexao = ConexaoPostgre()

    def createProdutor(self, produtor):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""INSERT INTO tb_produtor (
                      nome
                  ) VALUES (
                      '{produtor.getNome()}'
                  ) RETURNING id_produtor;"""

        cur.execute(sql)
        id_produtor = cur.fetchone()[0]  
        produtor.setIdProdutor(id_produtor)  

        con.commit()
        con.close()
        
        return produtor

    def readProdutores(self):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_produtor, 
                         nome
	              FROM tb_produtor;"""

        cur.execute(sql)
        listaProdutorBanco = cur.fetchall()
        listaProdutorEntidade = self.converterListaBancoParaListaEntidade(
listaProdutorBanco)
        con.close()
        return listaProdutorEntidade

    def readProdutor(self, id_produtor):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_produtor, 
                         nome
	              FROM tb_produtor
                  WHERE tb_produtor.id_produtor = {id_produtor};"""

        cur.execute(sql)
        produtorBanco = cur.fetchall()
        con.close()

        if len(produtorBanco) > 0:
            produtorEntidade = self.converterBancoParaEntidade(
                produtorBanco[0])
            return produtorEntidade
        else:
            return None

    def readProdutorPorNome(self, nome):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_produtor, 
                         nome
	              FROM tb_produtor
                  WHERE UPPER(tb_produtor.nome) = '{nome.upper()}';"""

        cur.execute(sql)
        produtorBanco = cur.fetchall()
        con.close()

        if len(produtorBanco) > 0:
            produtorEntidade = self.converterBancoParaEntidade(produtorBanco[0])
            return produtorEntidade
        else:
            return None

    def updateProdutor(self, produtor):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""UPDATE tb_produtor
                  SET nome='{produtor.getNome()}'
	              WHERE tb_produtor.id_produtor = {produtor.getIdProdutor()};"""

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        con.close()
        return produtor

    def deleteProdutor(self, id_produtor):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""DELETE FROM tb_produtor
	              WHERE tb_produtor.id_produtor = {id_produtor};"""

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        con.close()

    def converterBancoParaEntidade(self, produtorBanco):
        produtorEntidade = Produtor()
        produtorEntidade.setIdProdutor(produtorBanco[0])
        produtorEntidade.setNome(produtorBanco[1])
        return produtorEntidade

    def converterListaBancoParaListaEntidade(self, listaProdutorBanco):
        listaProdutorEntidade = []
        for produtorBanco in listaProdutorBanco:
            listaProdutorEntidade.append(
                self.converterBancoParaEntidade(produtorBanco))
        return listaProdutorEntidade

    def nomeJaExiste(self, produtor):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT count(1)
	              FROM tb_produtor
                  WHERE tb_produtor.nome = '{produtor.getNome()}' """

        if produtor.getIdProdutor() != None:
            sql += f"AND tb_produtor.id_produtor != {produtor.getIdProdutor() }"

        cur.execute(sql)
        qtdProdutores = cur.fetchall()
        con.close()

        if qtdProdutores[0][0] > 0:
            return True
        else:
            return False
