listaRevistas = []
listaAmigos = []
listaEmprestimo = []

from random import randint
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

    print(f'{"-----------------------"}')
    print(f'{"# Cadastro de Revista #"}')
    print(f'{"-----------------------"}')
    colecao = str(input('Coleção: ')).title().strip()
    c = 0
    if len(listaRevistas) == 0:
        edicao = randint(1111, 9999)
    else:
        edicao = randint(1111, 9999)
        while listaRevistas[c].edicao == edicao:
            edicao = randint(1111, 9999)
            c += 1
    print('Edição: ', end='')
    print(edicao)
    ano = validarInt('Ano: ')
    print(f'{"-----------------------"}')

    r = revista(colecao, edicao, ano, situacao=False)

    listaRevistas.append(r)

    return r


def imprimirListaRevistas():
    print(f'{"---------------------"}')
    print(f'{"# Lista de Revistas #"}')
    print(f'{"---------------------"}')
    for c in range(0, len(listaRevistas)):
        print(f'{"-" * 50}')
        print(f'Coleção: {listaRevistas[c].colecao}\n'
              f'Edição: {listaRevistas[c].edicao}\n'
              f'Ano: {listaRevistas[c].ano}')
    print(f'{"---------------------"}')


def validarInt(n):
    while True:
        try:
            nn = int(input(n))
        except (ValueError, TypeError):
            print('\033[0;31mErro! Digite um número válido.\033[m')
            continue
        else:
            return nn


def validarNome(s):
    while True:
        n = input(s).strip()
        if n.isalpha() or n.replace(' ', '').isalpha():
            break
        else:
            print('\033[0;31mErro! Digite apenas Letras para Nome e Sobrenome.\033[m')
            continue
    return n.title()


def validarTelefoneCelular(s):
    while True:
        qn = 0
        sn = ''
        nt = input(s).strip()
        for c in range(0, len(nt)):
            if nt[c].isnumeric():
                qn += 1
                sn += nt[c]
        if qn != 11:
            print('\033[0;31mNúmero Inválido!\033[m \033[0;33mPrecisa ter 11 números...\n'
                  'Exemplo: (53) 98765-4321\033[m')
            continue
        else:
            break
    return sn


def pause():
    input('Pressione \033[0;32mENTER\033[m para continuar...')


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

    print(f'{"---------------------"}')
    print(f'{"# Cadastro de Amigo #"}')
    print(f'{"---------------------"}')
    nome = validarNome('Nome: ')
    telefone = validarTelefoneCelular('Telefone Celular: ')
    endereco = str(input('Endereço: '))
    print(f'{"---------------------"}')

    a = amigo(nome, telefone, endereco, locacao=False)

    listaAmigos.append(a)

    return a


def imprimirListaAmigos():
    print(f'{"-------------------"}')
    print(f'{"# Lista de Amigos #"}')
    print(f'{"-------------------"}')
    for c in range(0, len(listaAmigos)):
        print(f'{"-" * 50}')
        print(f'Nome: {listaAmigos[c].nome}\n'
              f'Telefone: ({listaAmigos[c].telefone[0]}{listaAmigos[c].telefone[1]}) '
              f'{listaAmigos[c].telefone[2]}{listaAmigos[c].telefone[3]}{listaAmigos[c].telefone[4]}'
              f'{listaAmigos[c].telefone[5]}{listaAmigos[c].telefone[6]}-{listaAmigos[c].telefone[7]}'
              f'{listaAmigos[c].telefone[8]}{listaAmigos[c].telefone[9]}{listaAmigos[c].telefone[10]}\n'
              f'Endereço: {listaAmigos[c].endereco}')
    print(f'{"-------------------"}')


from datetime import date, timedelta
def cadastrarEmprestimo():
    class emprestimo:
        def __init__(self, dataL, dataD, revista, amigo):
            self.dataL = dataL
            self.dataD = dataD
            self.revista = revista
            self.amigo = amigo

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

    print(f'{"--------------------------"}')
    print(f'{"# Cadastro de Empréstimo #"}')
    print(f'{"--------------------------"}')
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
                print('\033[0;31mErro! Escolha um COD válido.\033[m')
            elif listaRevistas[oR].situacao == True:
                print('\033[0;31mErro! Revista já está Emprestada.\033[m')
            else:
                revista = listaRevistas[oR]
                listaRevistas[oR].situacao = True
                break
        print('-' * 32)
        print(f'{"ESCOLHA UM AMIGO":^32}')
        print('-' * 32)
        print(f'{"cod":^5}{"nome":^20}{"locação":^7}')
        print('-' * 32)
        for c in range(0, len(listaAmigos)):
            if listaAmigos[c].locacao == False:
                print(f'{c+1:^5}{listaAmigos[c].nome:^20}\033[0;32m{"Não":^7}\033[m')
            else:
                print(f'{c + 1:^5}{listaAmigos[c].nome:^20}\033[0;33m{"Sim":^7}\033[m')
        print('-' * 32)
        while True:
            oA = validarInt('Amigo Cod: ') - 1
            if oA < 0 or oA > len(listaAmigos):
                print('\033[0;31mErro! Escolha um COD válido.\033[m')
            else:
                amigo = listaAmigos[oA]
                listaAmigos[oA].locacao = True
                break
        print('-' * 25)
        dataL = date.today().strftime('%d/%m/%Y')
        print(f'Locação: {dataL}')
        dataD = date.today() + timedelta(days=7)
        dataD = dataD.strftime('%d/%m/%Y')
        print(f'Devolução: {dataD}')
        print(f'{"--------------------------"}')
        break

    e = emprestimo(dataL, dataD, revista, amigo)

    listaEmprestimo.append(e)

    return e


def verificarSituacaoListaRevista():
    qD = len(listaRevistas)
    for c in range(0, len(listaRevistas)):
        if listaRevistas[c].situacao == True:
            qD -= 1
    if qD == 0:
        return False
    else:
        return True


def imprimirListaEmprestimos():
    print(f'{"------------------------"}')
    print(f'{"# Lista de Empréstimos #"}')
    print(f'{"------------------------"}')
    for c in range(0, len(listaEmprestimo)):
        print(f'{"-" * 50}')
        print(f'Revista: {listaEmprestimo[c].revista.colecao}, {listaEmprestimo[c].revista.edicao}, '
              f'{listaEmprestimo[c].revista.ano}\n'
              f'Amigo: {listaEmprestimo[c].amigo.nome}\n'
              f'Locação: {listaEmprestimo[c].dataL}\n'
              f'Devolução: {listaEmprestimo[c].dataD}')
    print(f'{"------------------------"}')

