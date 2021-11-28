from Servicos.SwapiService import SwapiService
import os
import json
from Servicos.FilmesServico import FilmesServico
from Servicos.UsuariosServico import UsuariosServico
from Servicos.ProdutoresServico import ProdutoresServico
import zipfile as zip


class GeralControlador:
    def __init__(self):
        self.produtoresServico = ProdutoresServico() 
        self.filmesServico = FilmesServico()        
        self.usuariosServico = UsuariosServico()
        self.SwapiService = SwapiService()
    
    def exportarTodosOsDados(self):
        produtores = self.produtoresServico.readProdutores()
        filmes = self.filmesServico.readFilmes()
        usuarios = self.usuariosServico.readUsuarios()

       
        listaTotal = {
            "produtores" : [produtor.__dict__ for produtor in produtores],
            "filmes": [filme.__dict__ for filme in filmes],
            "usuarios" : [usuario.__dict__ for usuario in usuarios],
        }
        listaTotalJson = json.dumps(listaTotal, ensure_ascii=False)

        dirDownloads = os.path.join(os.sep, os.path.expanduser('~') , 'Downloads', )
        dir = os.path.join(os.sep, dirDownloads, 'DadosExportadosTopEspInf.zip')
        
        arquivoZip = zip.ZipFile(dir, 'w')
        arquivoZip.writestr('DadosExportadosTopEspInf.json', listaTotalJson)
        arquivoZip.close()
        
    def readFilmesApiSwapi(self):
        filmesApi = self.SwapiService.readFilmesApiSwapi()
        filmes = self.SwapiService.converteFilmesApiParaFilmesDTO(filmesApi)
        return filmes
    
    def createFilmeApiSwapi(self, filme):
        self.SwapiService.createFilmeApiSwapi(filme)