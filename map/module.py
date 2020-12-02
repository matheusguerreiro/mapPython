listaRevistas = []
listaAmigos = []
listaEmprestimo = []

def cadastrarRevista():
    class revista:
        def __init__(self, colecao, edicao, ano, situacao):
            self.colecao = colecao
            self.edicao = edicao
            self.ano = ano
            self.situacao = situacao

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

        def setLocada(self, situacao):
            self.locada = situacao
        def getLocada(self):
            return self.locada

    colecao = str(input('Coleção: ')).title().strip()
    edicao = validarInt('Edição: ')
    ano = validarInt('Ano: ')

    r = revista(colecao, edicao, ano, situacao=False)

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
            nn = int(input(n))
        except (ValueError, TypeError):
            print('Erro! Digite um número válido.')
            continue
        else:
            return nn


def pause():
    input('Pressione Enter para continuar...')


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

    nome = str(input('Nome: ')).title().strip()
    telefone = str(input('Telefone: '))
    endereco = str(input('Endereço: '))

    a = amigo(nome, telefone, endereco, locacao=False)

    listaAmigos.append(a)

    return a


def imprimirListaAmigos():
    for c in range(0, len(listaAmigos)):
        print(f'{"-------------------------------"}')
        print(f'Nome: {listaAmigos[c].nome}\n'
              f'Telefone: {listaAmigos[c].telefone}\n'
              f'Endereço: {listaAmigos[c].endereco}\n')
        print(f'{"-------------------------------"}')


def cadastrarEmprestimo():
    class emprestimo:
        def __init__(self, dataL, dataD, amigo, revista):
            self.dataL = dataL
            self.dataD = dataD
            self.amigo = amigo
            self.revista = revista

        def setDataL(self, dataL):
            self.dataL = dataL
        def getDataL(self):
            return self.dataL

        def setDataD(self, dataD):
            self.dataD = dataD
        def getDataD(self):
            return self.dataD

        def setAmigo(self, amigo):
            self.amigo = amigo
        def getAmigo(self):
            return self.amigo

        def setRevista(self, revista):
            self.revista = revista
        def getRevista(self):
            return self.revista


        while True:
            print('-'*51)
            print(f'{"ESCOLHA UMA REVISTA":^51}')
            print('-'*51)
            print(f'{"cod":^5}{"coleção":^20}{"edição":^8}{"ano":^6}{"situação":^12}')
            print('-'*51)
            for c in range(0, len(listaRevistas)):
                if listaRevistas[c].situacao == False:
                    print(f'{c+1:^5}{listaRevistas[c].colecao:^20}{listaRevistas[c].edicao:^8}{listaRevistas[c].ano:^6}'
                          f'\033[0;32m{"Disponível":^12}\033[m')
                else:
                    print(
                        f'{c+1:^5}{listaRevistas[c].colecao:^20}{listaRevistas[c].edicao:^8}{listaRevistas[c].ano:^6}'
                        f'\033[0;31m{"Emprestada":^12}\033[m')
            print('-' * 51)
            while True:
                oR = validarInt('Revista Cod: ') - 1
                if oR < 0 or oR > len(listaRevistas):
                    print('Erro! Escolha um COD válido.')
                else:
                    revista = listaRevistas[oR]
                    break
            print('-' * 25)
            print(f'{"ESCOLHA UM AMIGO":^25}')
            print('-' * 25)
            print(f'{"cod":^5}{"nome":^20}')
            print('-' * 25)
            for c in range(0, len(listaAmigos)):
                print(f'{c+1:^5}{listaAmigos[c].nome:^20}')
            print('-' * 25)
            pause()
            break

def imprimirListaEmprestimos():
    print(listaEmprestimo)


