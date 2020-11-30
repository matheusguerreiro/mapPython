from module import *
from time import sleep

while True:
    print(f'{"-------------------------------"}')
    print(f'{"### EMPRÉSTIMO DE REVISTAS  ###"}')
    print(f'{"-------------------------------"}')
    print(f'{"(1) Cadastrar Revista"}')
    print(f'{"(2) Cadastrar Amigo"}')
    print(f'{"(3) Cadastrar Empréstimo"}')
    print(f'{"(4) Ver Lista de Revistas"}')
    print(f'{"(5) Ver Lista de Amigos"}')
    print(f'{"(6) Ver Lista de Empréstimos"}')
    print(f'{"(7) Sair"}')
    print(f'{"-------------------------------"}')
    opcao = validarInt('Opção: ')

    if opcao == 1:
        cadastrarRevista()
    elif opcao == 2:
        cadastrarAmigo()
    elif opcao == 3:
        if len(listaRevistas) == 0 or len(listaAmigos) == 0:
            if len(listaRevistas) == 0:
                print('Erro! Não temos Nenhuma revista Cadastrada.')
                print('Cadastre uma Revista primeiro.')
            else:
                print('Erro! Não temos Nenhum amigo Cadastrado.')
                print('Cadastre um Amigo primeiro.')
        else:
            cadastrarEmprestimo()
    elif opcao == 4:
        if len(listaRevistas) == 0:
            print('A Lista de Revistas está Vazia!')
            pause()
        else:
            imprimirListaRevistas()
            pause()
    elif opcao == 5:
        if len(listaAmigos) == 0:
            print('A Lista de Amigos está Vazia!')
        else:
            imprimirListaAmigos()
    elif opcao == 6:
        if len(listaEmprestimo) == 0:
            print('A Lista de Empréstimos está Vazia!')
        else:
            imprimirListaEmprestimos()
    elif opcao == 7:
        print('Saindo...')
        sleep(1)
        break
    else:
        print('Erro! Digite uma Opção Válida.\n'
              'Opções de 1 até 7')

