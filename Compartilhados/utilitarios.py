class utilitarios:
    
    def listarPorExtenso(lista):
        listaPorExtenso = ""
        for i in range(len(lista)):
            if i == len(lista):
                listaPorExtenso += str(i)
            else:
                listaPorExtenso += f'{str(i)}, '