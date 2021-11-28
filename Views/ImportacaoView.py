import os
from Views.FilmesView import FilmesView
from Controladores.GeralControlador import GeralControlador
from Views.Compartilhados.UtilitariosView import utilitariosView


class ImportacaoView:
    def __init__(self):
        self.utilView = utilitariosView()
        self.geralControlador = GeralControlador()
        self.filmesView = FilmesView()
    
    def importarFilme(self):
        u = self.utilView
        os.system('cls')
        try:
            filmesSwapi = self.geralControlador.readFilmesApiSwapi()
            self.filmesView.imprimir(filmesSwapi, filmesDTO=True)

            u.printInstrucao('Digite o ID do filme que deseja importar (digite 0 para cancelar):')
            op = self.utilView.receberValor(chave="id do filme", tipo=int, obrigatorio=True, validos=lambda x: x == 0 or x in [n.getIdFilme() for n in filmesSwapi if n.getIdFilme() == x])
            
            if op != 0:
                self.geralControlador.createFilmeApiSwapi([n for n in filmesSwapi if n.getIdFilme() == op][0])
                os.system('cls')
                u.printSeparador(f'{"="*70}') 
                u.printSucesso('O filme foi importado com sucesso!')  
                u.printSeparador(f'{"="*70}')
                os.system('pause') 
        except Exception as ex:     
            os.system('cls')               
            u.printSeparador(f'{"="*70}')
            u.printErro('Erro ao importar o filme! Tente novamente.')
            u.printErro(F'ERRO: {ex}')
            u.printSeparador(f'{"="*70}') 
            os.system('pause')
