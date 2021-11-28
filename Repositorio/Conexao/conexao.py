import psycopg2 as pg

class ConexaoPostgre:
    def conectar(self):
        self.con = pg.connect(
                database="db_topicos_especiais_de_informatica",
                user="postgres",
                password="admin",
                host="127.0.0.1",
                port="5432"
        )        
        return self.con
