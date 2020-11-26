Revistas = {}
listaRevistas = []
Amigos = {}
listaAmigos = []

def cadastrarRevista():
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

    Revistas.clear()

    Revistas['Coleção'] = r.getColecao()
    Revistas['Edição'] = r.getEdicao()
    Revistas['Ano'] = r.getAno()

    listaRevistas.append(Revistas.copy())

    return r


def validarInt(n):
    while True:
        try:
            o = int(input(n))
        except (ValueError, TypeError):
            print('Erro! Digite um número válido.')
            continue
        else:
            return o


def cadastrarAmigo():
    class amigo:
        def __init__(self, nome, telefone, endereco):
            self.nome = nome
            self.telefone = telefone
            self.endereco = endereco

        def setNome(self, nome):
            self.nome = nome
        def getNome(self):
            return self.nome

        def setTelefone(self, telefone):
            self.telefone = telefone
        def getTelefone(self):
            return self.telefone

        def setEndereco(self, endereco):
            self.endereco = endereco
        def getEndereco(self):
            return self.endereco

    nome = str(input('Nome: '))
    telefone = str(input('Telefone: '))
    endereco = str(input('Endereço: '))

    a = amigo(nome, telefone, endereco)
    listaAmigos.append(a[:])
    return a


def cadastrarEmprestimo():
    class emprestimo:
        def __init__(self, dataL, dataD):
            self.dataL = dataL
            self.dataD = dataD


