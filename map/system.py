def criarRevista():
    class revista:
        def __init__(self, colecao, edicao, ano):
            self.colecao = colecao
            self.edicao = edicao
            self.ano = ano

        def setColecao(self, colecao):
            self.colecao = colecao
        def getColecao(self):
            return self.colecao

        def setEdicao(self, edicao):
            self.edicao = edicao
        def getEdicao(self):
            return self.edicao

        def setAno(self, ano):
            self.ano = ano
        def getAno(self):
            return self.ano

    colecao = str(input('Coleção: '))
    edicao = int(input('Edição: '))
    ano = int(input('Ano: '))

    r = revista(colecao, edicao, ano)
    return r

