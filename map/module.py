listaRevistas = []
listaAmigos = []
listaEmprestimo = []

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

    colecao = str(input('Coleção: ')).title().strip()
    edicao = validarInt('Edição: ')
    ano = validarInt('Ano: ')

    r = revista(colecao, edicao, ano)

    listaRevistas.append(r)

    return r


def imprimirListaRevistas():
    for c in range(0, len(listaRevistas)):
        print(f'{"-------------------------------"}')
        print(f'Coleção: {listaRevistas[c].colecao}\n'
              f'Edição: {listaRevistas[c].edicao}\n'
              f'Ano: {listaRevistas[c].ano}')
        print(f'{"-------------------------------"}')


def validarInt(n):
    while True:
        try:
            o = int(input(n))
        except (ValueError, TypeError):
            print('Erro! Digite um número válido.')
            continue
        else:
            return o


def pause():
    print('Continuar?')
    wait = input('Pressione Enter para continuar...')


def cadastrarAmigo():
    class amigo:
        def __init__(self, nome, telefone, endereco, locacao):
            self.nome = nome
            self.telefone = telefone
            self.endereco = endereco
            self.locacao = locacao

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

        def setLocacao(self, locacao):
            self.locacao = locacao
        def getLocacao(self):
            return self.locacao

    nome = str(input('Nome: '))
    telefone = str(input('Telefone: '))
    endereco = str(input('Endereço: '))
    locacao = False

    a = amigo(nome, telefone, endereco, locacao)

    listaAmigos.append(a)

    return a


def imprimirListaAmigos():
    for c in range(0, len(listaAmigos)):
        print(f'{"-------------------------------"}')
        print(f'Nome: {listaAmigos[c].nome}\n'
              f'Telefone: {listaAmigos[c].telefone}\n'
              f'Endereço: {listaAmigos[c].endereco}\n'
              f'Locação: {listaAmigos[c].locacao}')
        print(f'{"-------------------------------"}')


def cadastrarEmprestimo():
    class emprestimo:
        def __init__(self, dataL, dataD, amigo, revista):
            self.dataL = dataL
            self.dataD = dataD
            self.amigo = amigo
            self.revista = revista


def imprimirListaEmprestimos():
    print(listaEmprestimo)


