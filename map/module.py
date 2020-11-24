def criarRevista():
    class revista:
        def __init__(self, colecao, edicao, ano):
            self.colecao = str(input('Coleção: '))
            self.edição = int(input('Edição: '))
            self.ano = int(input('Ano: '))

