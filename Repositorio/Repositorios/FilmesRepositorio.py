from Repositorio.Entidades.Filme import Filme
from Repositorio.Conexao.conexao import ConexaoPostgre

class FilmesRepositorio:
    def __init__(self):
        self.conexao = ConexaoPostgre()

    def createFilme(self, filme):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""INSERT INTO tb_filme (
                      id_produtor, 
                      titulo, 
                      diretor, 
                      ano_lancamento
                  ) VALUES (
                      {filme.getIdProdutor() if filme.getIdProdutor() != None else 'NULL'}, 
                      '{filme.getTitulo() if filme.getTitulo() != None else 'NULL'}', 
                      '{filme.getDiretor() if filme.getDiretor() != None else 'NULL'}',
                      '{filme.getAnoLancamento() if filme.getAnoLancamento() != None else 'NULL'}'
                  ) RETURNING id_filme;"""

        cur.execute(sql)           
        id_filme = cur.fetchone()[0]  
        filme.setIdFilme(id_filme)  

        con.commit()
        con.close()       

        return filme

    def readFilmes(self):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_filme, 
                         id_produtor, 
                         titulo, 
                         diretor, 
                         ano_lancamento
	              FROM tb_filme;"""

        cur.execute(sql)  
        listaFilmeBanco = cur.fetchall()
        listaFilmeEntidade = self.converterListaBancoParaListaEntidade(
            listaFilmeBanco)
        con.close()
        return listaFilmeEntidade
        
    def readFilme(self, id_filme):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT id_filme, 
                         id_produtor, 
                         titulo, 
                         diretor, 
                         ano_lancamento
	              FROM tb_filme
                  WHERE tb_filme.id_filme = {id_filme};"""

        cur.execute(sql)  
        filmeBanco = cur.fetchall()      
        con.close()
        
        if len(filmeBanco) > 0:
            filmeEntidade = self.converterBancoParaEntidade(
                filmeBanco[0])
            return filmeEntidade
        else:
            return None

    def updateFilme(self, filme):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""UPDATE tb_filme
	              SET id_produtor={filme.getIdProdutor() if filme.getIdProdutor() != None else 'NULL'},
                      titulo='{filme.getTitulo() if filme.getTitulo() != None else 'NULL'}', 
                      diretor='{filme.getDiretor() if filme.getDiretor() != None else 'NULL'}', 
                      ano_lancamento='{filme.getano_lancamento() if filme.getano_lancamento() != None else 'NULL'}'
	              WHERE tb_filme.id_filme = {filme.getIdFilme() if filme.getIdFilme() != None else 'NULL'};"""

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        con.close()
        return filme

    def deleteFilme(self, id_filme):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""DELETE FROM tb_filme
	              WHERE tb_filme.id_filme = {id_filme};"""

        cur = con.cursor()
        cur.execute(sql)
        con.commit()

        con.close()
    
    def converterBancoParaEntidade(self, filmeBanco):
        filmeEntidade = Filme()
        filmeEntidade.setIdFilme(filmeBanco[0])
        filmeEntidade.setIdProdutor(filmeBanco[1])
        filmeEntidade.setTitulo(filmeBanco[2])
        filmeEntidade.setDiretor(filmeBanco[3])
        filmeEntidade.setAnoLancamento(filmeBanco[4])
        return filmeEntidade

    def converterListaBancoParaListaEntidade(self, listaFilmeBanco):
        listaFilmeEntidade = []
        for filmeBanco in listaFilmeBanco:
            listaFilmeEntidade.append(self.converterBancoParaEntidade(filmeBanco))
        return listaFilmeEntidade
    
    def tituloJaExiste(self, filme):
        con = self.conexao.conectar()
        cur = con.cursor()

        sql = f"""SELECT count(1)
	              FROM tb_filme
                  WHERE tb_filme.titulo = '{filme.getTitulo()}' """

        if filme.getIdFilme() != None:
            sql += f"AND tb_filme.id_filme != {filme.getIdFilme()}"

        cur.execute(sql)  
        qtdFilmes = cur.fetchall()      
        con.close()
        
        if qtdFilmes[0][0] > 0:            
            return True
        else:
            return False