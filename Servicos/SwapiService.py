from Repositorio.Entidades.Filme import Filme
from Repositorio.Entidades.Produtor import Produtor
from Controladores.ProdutoresControlador import ProdutoresControlador
from Controladores.FilmesControlador import FilmesControlador
import requests
from Repositorio.DTO.DTOFilmeSwapi import DTOFilmeSwapi


class SwapiService:
    def __init__(self):
        self.FilmesControlador = FilmesControlador()
        self.produtoresControlador = ProdutoresControlador()
        self.url_filmes = 'https://swapi.dev/api/films/'
        
    def readFilmesApiSwapi(self):        
        respostaAPI = requests.get(url=self.url_filmes)
        filmesApi = respostaAPI.json()['results']
        return filmesApi        
    
    def converteFilmesApiParaFilmesDTO(self, filmesApi):
        filmeDTOs = [self.converteFilmeApiParaFilmeDTO(v) for v in filmesApi]
        return filmeDTOs
    
    def converteFilmeApiParaFilmeDTO(self, filmeApi):
        filmeDTO = DTOFilmeSwapi()
        filmeDTO.setIdFilme(int(filmeApi['url'].replace('https://swapi.dev/api/films/', '').replace('/', '')))
        filmeDTO.setNomeProdutor(filmeApi['producer'])
        filmeDTO.setTitulo(filmeApi['title'])
        filmeDTO.setDiretor(filmeApi['director'])
        filmeDTO.setAnoLancamento(filmeApi['release_date'])
        return filmeDTO

    def createFilmeApiSwapi(self, filmeDTO):
        filmeEntidade = self.converteFilmeDTOParaFilmeEntidade(filmeDTO)
        self.FilmesControlador.createFilme(filmeEntidade)
    
    def converteFilmeDTOParaFilmeEntidade(self, filmeDTO):
        produtor = self.produtoresControlador.readProdutorPorNome(filmeDTO.getNomeProdutor())
        if produtor == None:
            produtor = Produtor()
            produtor.setNome(filmeDTO.getNomeProdutor())
            produtor = self.produtoresControlador.createProdutor(produtor)

        filmeEntidade = Filme()
        filmeEntidade.setIdFilme(int(filmeDTO.getIdFilme()))
        filmeEntidade.setIdProdutor(produtor.getIdProdutor())
        filmeEntidade.setTitulo(filmeDTO.getTitulo())
        filmeEntidade.setDiretor(filmeDTO.getDiretor())
        filmeEntidade.setAnoLancamento(filmeDTO.getAnoLancamento())
        return filmeEntidade